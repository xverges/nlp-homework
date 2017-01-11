# vim: set fileencoding=UTF-8

import unittest
import langid
from nose_parameterized import parameterized

class TestLanguageDetectors(unittest.TestCase):

    def test_basic_spanish(self):
        id = langid.classify('Una primera prueba en español')[0]
        self.assertEquals('es', id)

    def test_basic_english(self):
        id = langid.classify('This is test for English')[0]
        self.assertEquals('en', id)

    @parameterized.expand([
        ("wikipedia1", "La dispraxia es una enfermedad psicomotriz que implica una falta de organización del movimiento"),
        ("wikipedia2", "El problema afecta tanto a la producción de sonidos como a la secuencializacion de los mismos")
    ])
    def test_spanish(self, _, text):
        id = langid.classify(text)[0]
        self.assertEquals('es', id)

    @parameterized.expand([
        (None, "Various areas of development can be affected by developmental coordination disorder"),
        (None, "Developmental coordination disorder is associated with problems with memory")
    ])
    def test_english(self, _, text):
        id = langid.classify(text)[0]
        self.assertEquals('en', id)

if __name__ == '__main__':
    unittest.main(verbosity=2)
