#method readInWords that takes a file path(to the file with words) as an argument and returns a list of words longer than 5 letters.
#initialize variable listOfWords and set it to empty list

#initailize variable fileWithWords and set it to the opened file
#initialize varialbe wordsFromFile and use readlines method to set it to the list of words from fileWithWords

#iterate over each word in wordsFromFile
#initialize variable strippedWord and set it to word without whitespaces (use strip method)
#check if length of strippedWord is greater than 5. If it is add it to listOfWords

#return listOfWords at the end of readInWords method

def readInWords():
    listOfWords = []
    filewithwords=open(r"wordsEn.txt")
    wordsdfromfile=filewithwords.readlines()
    for word in wordsdfromfile:
        strippedWord=word.strip()
        if len(strippedWord)>5:
            listOfWords.append(strippedWord)

    return listOfWords


#method that takes a letter and word as an argument and returns true if a word contains letter
#method will only perform a check if a letter and word are not empty strings. It will return False if word and letter are empty strings
def letterInWord(word, letter):
    pass


#method that takes a list of words as an argument and returns one, randomly chosen word
def selectAWordToGuess(wordsList):
    pass

