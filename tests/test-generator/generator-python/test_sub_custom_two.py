'''
An example of a couple of custom tests. All custom tests derive from TestBaseClass.
'''
from test_base_class import TestBaseClass

class CustomTestThree(TestBaseClass):
    def generate(self):

        output = {}
        output['v1'] = 323.50
        output['v2'] = 7
        output['v3'] = False

        return output

class CustomTestFour(TestBaseClass):
    def generate(self):

        output = {}
        output["intValue"] = 43
        output["floatValue"] = 3.14159265358979
        output["timeValue"] = "2018-10-09T20:21:51.039Z"
        output["boolValue"] = True
        output["stringValue"] = "abc% - &XYZ"

        return output
