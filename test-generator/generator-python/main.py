import sys
import os
import json
import pickle
import test_sub_builtIn
import of_sub_event_hub

def load_config():
    '''
    loads the json configuration file
    '''
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config

def get_tests_from_configuration(input_type):

    # get the configuration
    harness_config = load_config()

    # initialize the list of required plugins
    required_plugins = []

    # get the list of tests from the configuration
    loaded_tests = harness_config['tests']

    # loop through the tests and get the required plugins
    for loaded_test in loaded_tests:
        if loaded_test['input']['type'] == input_type:
            required_plugins.append(loaded_test['assembly'])

    # eliminate duplicates from the list of required plugins
    unique_plugins = list(set(required_plugins))

    # get the test classes in the plugins
    test_classes_in_plugins = []
    for plugin in unique_plugins:
        test_classes_in_plugins += pickle.load(open( plugin + ".p", "rb" ))

    # make a list of dictionary to return - have to add a couple of attributes
    # need the input_type for all, filename for file inputs.
    tests_to_return = []
    for loaded_test in loaded_tests:       
        test_typename = loaded_test['type']
        if (loaded_test['input']['type'] == input_type) and (input_type == 'plugin'):
            tests_to_return.append(
                {
                    'input_type': 'plugin', 
                    'class': [elem for elem in test_classes_in_plugins if elem.__name__ == test_typename][0],
                    'typename': test_typename
                }
            )
        elif (loaded_test['input']['type'] == input_type) and (input_type == 'file'):
            tests_to_return.append(
                {
                    'input_type': 'file', 
                    'class': [elem for elem in test_classes_in_plugins if elem.__name__ == test_typename][0],
                    'filename': loaded_test['input']['filename'],
                    'typename': test_typename
                }
            )

    # return that list to the caller
    return tests_to_return

def load_tests_from_plugins():

    tests_in_plugins = get_tests_from_configuration('plugin')
    tests_in_plugins += get_tests_from_configuration('file')
 
    # return that list to the caller
    return tests_in_plugins

def invoke_tests():
    '''
        invokes each of the pickled custom tests in turn to get generated test output
        transmits the test output to the configured event hub
    '''

    loaded_tests = load_tests_from_plugins()

    output_formatter = of_sub_event_hub.EventHubOutputFormatter()

    try: 
        for test in loaded_tests:
            instance = test['class']()
            if test['input_type'] == 'plugin':
                output_formatter.send(instance.generate())
                print('Sending message from ' + test['typename'])
            elif test['input_type'] == 'file':
                output_formatter.send(instance.generate(test['filename']))
                print('Sending message from ' + test['typename'] + ', filename: ' + test['filename'])
    except Exception as e:
        raise e       
    finally:
        output_formatter.close()

if __name__ == "__main__":
    invoke_tests()
