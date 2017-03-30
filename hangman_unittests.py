import unittest
import hangman

class TestStringMethods(unittest.TestCase):

    def test_readInWords(self):
        wordsList = hangman.readInWords('wordsEn.txt')
        self.assertEqual(len(wordsList), 521)

    def test_letterInWord(self):
        self.assertTrue(hangman.letterInWord("AAA", 'A'))
        self.assertTrue(hangman.letterInWord("AAA", 'a'))
        self.assertFalse(hangman.letterInWord("AAA", 'B'))
        self.assertFalse(hangman.letterInWord("AAA", 'b'))
        self.assertFalse(hangman.letterInWord("", 'b'))
        self.assertFalse(hangman.letterInWord("AAA", ''))
        self.assertFalse(hangman.letterInWord("", ''))

    def test_selectAWordToGuessValid(self):
        validWordsList = ['aaa', 'b', 'cc', 'Ddddd']
        self.assertTrue(len(hangman.selectAWordToGuess(validWordsList)) != 0)
        self.assertTrue(type(hangman.selectAWordToGuess(validWordsList)) == str)
        self.assertTrue(hangman.selectAWordToGuess(validWordsList)in validWordsList)

    def test_selectAWordToGuessInvalid(self):
        self.assertEqual(hangman.selectAWordToGuess([]), '')

if __name__ == '__main__':
    unittest.main()