# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# -----------------------------------------------------------------------------------

"""
Eventhub Event Processor Module
"""

import logging
import asyncio
import os
import dotenv

from azure.eventprocessorhost import (
    AbstractEventProcessor,
    AzureStorageCheckpointLeaseManager,
    EventHubConfig,
    EventProcessorHost,
    EPHOptions)

import datatransformer
import blobsender

logger = logging.getLogger(__name__)

class EventProcessor(AbstractEventProcessor):
    """
    Data Pipeline Event Processor
    """

    def __init__(self, params=None):
        """
        Init Event processor
        """
        super().__init__(params)
        self._msg_counter = 0


    async def open_async(self, context):
        """
        Called by processor host to initialize the event processor.
        """
        logger.info("Connection established {}".format(context.partition_id))


    async def close_async(self, context, reason):
        """
        Called by processor host to indicate that the event processor is being stopped.
        :param context: Information about the partition
        :type context: ~azure.eventprocessorhost.PartitionContext
        """
        logger.info("Connection closed (reason {}, id {}, offset {}, sq_number {})".format(
            reason,
            context.partition_id,
            context.offset,
            context.sequence_number))


    async def process_events_async(self, context, messages):
        """
        Called by the processor host when a batch of events has arrived.
        This is where the real work of the event processor is done.
        :param context: Information about the partition
        :type context: ~azure.eventprocessorhost.PartitionContext
        :param messages: The events to be processed.
        :type messages: list[~azure.eventhub.common.EventData]
        """
        logger.info("Events processed {}".format(context.sequence_number))
        logger.info("Message: {}".format(messages))
        for message in messages:
            body = message.body_as_str()
            logger.info("MESSAGE BODY: {}".format(body))
            transformed_body = datatransformer.transform(body)
            logger.info("MESSAGE TRANSFORMED BODY: {}".format(transformed_body))
            blobsender.uploadblob(transformed_body)
        await context.checkpoint_async()


    async def process_error_async(self, context, error):
        """
        Called when the underlying client experiences an error while receiving.
        EventProcessorHost will take care of recovering from the error and
        continuing to pump messages,so no action is required from
        :param context: Information about the partition
        :type context: ~azure.eventprocessorhost.PartitionContext
        :param error: The error that occured.
        """
        logger.error("Event Processor Error {!r}".format(error))


async def wait_and_close(host):
    """
    Run EventProcessorHost indefinetely
    """
    while True:
        await asyncio.sleep(1)


def main():
    """
    Main method of this module
    """
    try:
        loop = asyncio.get_event_loop()

        # Storage Account Credentials
        storage_account_name = os.environ.get('AZURE_STORAGE_ACCOUNT')
        storage_key = os.environ.get('AZURE_STORAGE_ACCESS_KEY')
        storage_container_lease = os.environ.get('EVENT_HUB_STORAGE_CONTAINER')

        namespace = os.environ.get('EVENT_HUB_NAMESPACE')
        eventhub = os.environ.get('EVENT_HUB_NAME')
        user = os.environ.get('EVENT_HUB_SAS_POLICY')
        key = os.environ.get('EVENT_HUB_SAS_KEY')
        consumer_group = os.environ.get('EVENT_HUB_CONSUMER_GROUP')

        # Eventhub config and storage manager
        eh_config = EventHubConfig(namespace, eventhub, user, key, consumer_group=consumer_group)
        eh_options = EPHOptions()
        eh_options.release_pump_on_timeout = True
        eh_options.debug_trace = False
        storage_manager = AzureStorageCheckpointLeaseManager(
            storage_account_name, storage_key, storage_container_lease)

        # Event loop and host
        host = EventProcessorHost(
            EventProcessor,
            eh_config,
            storage_manager,
            ep_params=[],
            eph_options=eh_options,
            loop=loop)

        tasks = asyncio.gather(
            host.open_async(),
            wait_and_close(host))

        loop.run_until_complete(tasks)

    except KeyboardInterrupt:
        # Canceling pending tasks and stopping the loop
        for task in asyncio.Task.all_tasks():
            task.cancel()
        loop.run_forever()
        tasks.exception()

    finally:
        loop.stop()


if __name__ == '__main__':
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)
    dotenv.load_dotenv('.env')

    # Run
    main()
