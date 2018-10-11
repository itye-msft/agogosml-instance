"""
Unit tests of the project
"""

import unittest
import json
import datatransformer

class TestUM(unittest.TestCase):
    """
    Tests of the Sample App
    """
    def setUp(self):
        """
        Setup of tests
        """
        pass

    def test_datatransformer(self):
        """
        Test that the data transformer transforms the data properly
        """
        transformed = datatransformer.transform('{"intValue": 1 }')
        parsed_json = json.loads(transformed)
        int_value = parsed_json['intValue']
        self.assertEqual(int_value, 2)

if __name__ == '__main__':
    unittest.main()
