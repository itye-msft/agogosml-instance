#!/usr/bin/env python

import sys
import logging
import datetime
import time
import os

import dotenv

from azure.eventhub import EventHubClient, Sender, EventData

# import examples

def main():
    logger = logging.getLogger(__name__)
    # Address can be in either of these formats:
    # "amqps://<URL-encoded-SAS-policy>:<URL-encoded-SAS-key>@<mynamespace>.servicebus.windows.net/myeventhub"
    # "amqps://<mynamespace>.servicebus.windows.net/myeventhub"
    # ADDRESS = os.environ.get('EVENT_HUB_ADDRESS')

    NAMESPACE = os.environ['EVENT_HUB_NAMESPACE']
    EHNAME = os.environ['EVENT_HUB_NAME']
    ADDRESS = "amqps://" + NAMESPACE + ".servicebus.windows.net/" + EHNAME

    # SAS policy and key are not required if they are encoded in the URL
    USER = os.environ.get('EVENT_HUB_SAS_POLICY')
    KEY = os.environ.get('EVENT_HUB_SAS_KEY')

    try:
        if not ADDRESS:
            raise ValueError("No EventHubs URL supplied.")

        client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
        sender = client.add_sender(partition="0")
        client.run()
        try:
            start_time = time.time()
            for i in range(100):
                logger.info("Sending message: {}".format(i))
                sender.send(EventData(str(i)))
        except:
            raise
        finally:
            end_time = time.time()
            client.stop()
            run_time = end_time - start_time
            logger.info("Runtime: {} seconds".format(run_time))

    except KeyboardInterrupt:
        pass


if __name__  == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    dotenv.load_dotenv('.env')

    # print("These are the passed env vars:")
    # print(os.environ['AZURE_STORAGE_ACCOUNT'])
    # print(os.environ['AZURE_STORAGE_ACCESS_KEY'])
    # print(os.environ['EVENT_HUB_NAMESPACE'])
    # print(os.environ['EVENT_HUB_NAME'])
    # print(os.environ['EVENT_HUB_SAS_POLICY'])
    # print(os.environ['EVENT_HUB_SAS_KEY'])
    
    # Run
    main()