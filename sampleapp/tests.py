import unittest
import datatransformer
import json

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_datatransformer(self):
        transformed = datatransformer.transform('{"intValue": 1 }')
        parsed_json = json.loads(transformed)
        intValue = parsed_json['intValue']
        self.assertEqual(intValue, 2)

if __name__ == '__main__':
    unittest.main()