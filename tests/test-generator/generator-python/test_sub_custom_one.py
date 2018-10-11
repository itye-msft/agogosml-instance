'''
An example of a couple of custom tests. All custom tests derive from TestBaseClass.
'''
from test_base_class import TestBaseClass

class CustomTestOne(TestBaseClass):
    def generate(self):

        output = {}
        output['v1'] = 123.50
        output['v2'] = 1
        output['v3'] = True

        return output

class CustomTestTwo(TestBaseClass):
    def generate(self):

        output = {}
        output["intValue"] = 42
        output["floatValue"] = 3.14159265358979
        output["timeValue"] = "2018-10-09T20:21:51.039Z"
        output["boolValue"] = False
        output["stringValue"] = "abc% - &XYZ"

        return output
