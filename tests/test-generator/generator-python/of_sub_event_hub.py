from azure.eventhub import EventHubClient, Sender, EventData
from of_base_class import OutputFormatterBaseClass
import os

class EventHubOutputFormatter(OutputFormatterBaseClass):
    def __init__(self):
        NAMESPACE = os.environ['EVENT_HUB_NAMESPACE']
        EHNAME = os.environ['EVENT_HUB_NAME']
        ADDRESS = "amqps://" + NAMESPACE + ".servicebus.windows.net/" + EHNAME

        # SAS policy and key are not required if they are encoded in the URL
        USER = os.environ.get('EVENT_HUB_SAS_POLICY')
        KEY = os.environ.get('EVENT_HUB_SAS_KEY')

        self.client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
        self.sender = self.client.add_sender(partition="0")
        self.client.run()

    def send(self, message):
        self.sender.send(EventData(message))
        pass

    def close(self):
        self.client.stop()
        pass