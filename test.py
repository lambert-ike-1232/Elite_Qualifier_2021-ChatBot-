import unittest
from main import init_chat

class TestChatbot(unittest.TestCase):

    def test_odd_num(self):
        if init_chat() != "q":
          self.assertTrue(init_chat())
    

if __name__ == '__main__':
    unittest.main()

