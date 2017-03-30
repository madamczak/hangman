import pytest
import hangman

def test_readInWords():
    wordsList = hangman.readInWords('wordsEn.txt')
    assert len(wordsList) == 521

def test_letterInWord():
    assert hangman.letterInWord("AAA", 'A') == True
    assert hangman.letterInWord("AAA", 'B') == False
    assert hangman.letterInWord("AAA", 'b') == False
    assert hangman.letterInWord("", 'b') == False
    assert hangman.letterInWord("AAA", '') == False
    assert hangman.letterInWord("", '') == False

def test_selectAWordToGuessValid():
    validWordsList = ['aaa', 'b', 'cc', 'Ddddd']
    assert len(hangman.selectAWordToGuess(validWordsList)) != 0
    assert type(hangman.selectAWordToGuess(validWordsList)) == str
    assert hangman.selectAWordToGuess(validWordsList) in validWordsList
