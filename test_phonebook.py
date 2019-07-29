import unittest
from phonebook import Phonebook


class PhonebookCase(unittest.TestCase):
    def test_create_phonebook(self):
        phonebook = Phonebook()


if __name__ == '__main__':
    unittest.main()
