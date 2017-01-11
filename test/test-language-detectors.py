# vim: set fileencoding=UTF-8

import unittest
import langid

class TestLanguageDetectors(unittest.TestCase):

    def test_basic_spanish(self):
        id = langid.classify('Una primera prueba en español')[0]
        self.assertEquals('es', id)

    def test_basic_english(self):
        id = langid.classify('This is test for English')[0]
        self.assertEquals('en', id)

if __name__ == '__main__':
    unittest.main()
