#!/usr/bin/env python

"""
Simple Eventhub data sender
"""

import sys
import logging
import os

import dotenv

from azure.eventhub import EventHubClient, Sender, EventData

logger = logging.getLogger(__name__)

def main():
    """
    Main method of sender
    """

    namespace = os.environ['EVENT_HUB_NAMESPACE']
    ehname = os.environ['EVENT_HUB_NAME']
    address = "amqps://" + namespace + ".servicebus.windows.net/" + ehname

    # SAS policy and key are not required if they are encoded in the URL
    user = os.environ.get('EVENT_HUB_SAS_POLICY')
    key = os.environ.get('EVENT_HUB_SAS_KEY')

    try:
        if not address:
            raise ValueError("No EventHubs URL supplied.")

        client = EventHubClient(address, debug=False, username=user, password=key)
        sender = client.add_sender(partition="0")
        client.run()
        try:
            start_time = time.time()
            for i in range(100):
                message = '{ "intValue": ' + str(i) + ' }'
                logger.info("Sending message: {}".format(message))
                sender.send(EventData(message))
        except:
            raise
        finally:
            end_time = time.time()
            client.stop()
            run_time = end_time - start_time
            logger.info("Runtime: {} seconds".format(run_time))

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)
    dotenv.load_dotenv('.env')
    # Run
    main()
