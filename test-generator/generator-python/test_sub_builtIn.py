'''
The builtin test class. All custom tests derive from TestBaseClass.
'''
from test_base_class import TestBaseClass
import json

class builtin_test(TestBaseClass):
    '''
    The default test loads output from a provided filename.
    '''
    def generate(self, filename):
        with open(filename, 'r') as f:
            output = json.load(f)
        return output
