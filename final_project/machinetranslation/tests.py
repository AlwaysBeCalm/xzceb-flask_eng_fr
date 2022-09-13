import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def testEnglishToFrenchEmptyParam(self):
        self.assertEqual(english_to_french(""), 
                         "you must enter English text to translate")

    def testEnglishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def testFrenchToEnglishEmptyParam(self):
        self.assertEqual(french_to_english(""), 
                         "you must enter French text to translate")

    def testFrenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()
