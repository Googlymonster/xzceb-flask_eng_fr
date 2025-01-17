import unittest
from translator import english_to_french, french_to_english

class TestTranslatorMethods(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(translator.englishToFrench('Hello'),'')

    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(translator.frenchToEnglish('Bonjour'),'')