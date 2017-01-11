import unittest

class TestLanguageDetectors(unittest.TestCase):

    def test_red(self):
        self.assertFalse(True, 'blah blah')

    def test_green(self):
        self.assertTrue(True, 'blah blah')

if __name__ == '__main__':
    unittest.main()
