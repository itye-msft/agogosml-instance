from pykafka import KafkaClient
from of_base_class import OutputFormatterBaseClass
import os
import json
import IPython

class KafkaOutputFormatter(OutputFormatterBaseClass):
    def __init__(self):
        KAFKA_HOST_IP = os.environ['KAFKA_HOST_IP']
        KAFKA_HOST_PORT = os.environ['KAFKA_HOST_PORT']
        KAFKA_TOPIC = os.environ['KAFKA_TOPIC']
        
        client = KafkaClient(hosts=KAFKA_HOST_IP + ":" + KAFKA_HOST_PORT)
        topic = client.topics[KAFKA_TOPIC]
        self.producer = topic.get_producer(delivery_reports=False)

    def send(self, input_message):
        string_message = json.dumps(input_message)
        self.producer.produce(string_message.encode('utf-8'))

    def close(self):
        self.producer.stop()
