import unittest
import hello

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_hello_add_num(self):
        self.assertEqual(hello.add_num(6,6), 12)

if __name__ == '__main__':
    unittest.main()