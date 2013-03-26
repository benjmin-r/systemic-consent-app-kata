from mock import Mock
import sys
import unittest

from util import CliReader

class TestCliReader(unittest.TestCase):
    
    def test_input(self):
        mockedStdIn = Mock()
        mockedStdIn.readline.return_value = "Chinese"
        option1 = CliReader(mockedStdIn).readline()
        self.assertEqual("Chinese", option1)


if __name__ == "__main__":
    unittest.main()