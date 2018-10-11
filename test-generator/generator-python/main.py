import sys
import os
import json
import pickle
import test_sub_builtIn
from azure.eventhub import EventHubClient, Sender, EventData

def load_config():
    '''
    loads the json configuration file
    '''
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config

def load_tests_from_plugins():
    required_plugins = []
    harness_config = load_config()
    loaded_tests = harness_config['tests']
    for loaded_test in loaded_tests:
        if loaded_test['input']['type'] == 'plugin':
            required_plugins.append(loaded_test['assembly'])
    unique_plugins = list(set(required_plugins))
    test_classes_in_plugin = []
    for plugin in unique_plugins:
        test_classes_in_plugin += pickle.load(open( plugin + ".p", "rb" ))
    return test_classes_in_plugin

def invoke_tests():
    '''
        invokes each of the pickled custom tests in turn to get generated test output
        transmits the test output to the configured event hub
    '''
    NAMESPACE = os.environ['EVENT_HUB_NAMESPACE']
    EHNAME = os.environ['EVENT_HUB_NAME']
    ADDRESS = "amqps://" + NAMESPACE + ".servicebus.windows.net/" + EHNAME

    # SAS policy and key are not required if they are encoded in the URL
    USER = os.environ.get('EVENT_HUB_SAS_POLICY')
    KEY = os.environ.get('EVENT_HUB_SAS_KEY')

    client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
    sender = client.add_sender(partition="0")
    client.run()

    loaded_tests = load_tests_from_plugins()

    try:
        for test in loaded_tests:
            instance = test()
            sender.send(EventData(instance.generate()))
    except Exception as e:
        raise e       
    finally:
        client.stop()

if __name__ == "__main__":
    invoke_tests()
