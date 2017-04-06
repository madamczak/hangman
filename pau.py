# def fuzzBizz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FuzzBizz"
#     elif number % 5 == 0:
#         return "Bizz"
#     elif number % 3 == 0:
#         return "Fuzz"
#     else:
#         return number
# print fuzzBizz(4)

#==============================================================================================

# def fuzzBizz2(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FuzzBizz"
#     elif number % 5 == 0:
#         return "Bizz"
#     elif number % 3 == 0:
#         return "Fuzz"
#     else:
#         return number
#
# print fuzzBizz2(4)

#==============================================================================================

#method that counts how many integer value 1 is in the list. Takes one argument - lstToCheck
#initialize a variable howMany and set it to 0
#loop through elements in the list and check if it has value 1.
# if it does - add 1 to howMany variable
#return howMany at the end of the method

# def howManyOnes(lstToCheck):
#     howMany=0
#     for l in lstToCheck:
#         if l ==1:
#             howMany +=1 #DODAWANIE DO ZMIENNEJ W FUNKCJI
#     return howMany
# print howManyOnes([1,5,10,16])
# #     pass

#==============================================================================================

#method that takes two arguments Aarg, and Barg and checks if their sum is even.
#initialize variable sumOfAB and set it to the sum of Aarg and Barg
#check if the modulo of sumOfAB and 2 is equal to 0. Return True if it is.
#return False otherwise
#
# def isSumEven(Aarg, Barg):
#  sumofab=Aarg+Barg
#  if sumofab%2 ==0:
#      return True
#  else:
#      return False
#
# print isSumEven(5, 6)

if isSumEven(5,6) == False:
    return True

#==============================================================================================
#DO DOMU
#method readInWords that takes a file path(to the file with words) as an argument and returns a list of words longer than 5 letters.
#initialize variable listOfWords and set it to empty list

#initailize variable fileWithWords and set it to the opened file
#initialize varialbe wordsFromFile and use readlines method to set it to the list of words from fileWithWords

#iterate over each word in wordsFromFile
#initialize variable strippedWord and set it to word without whitespaces (use strip method)
#check if length of strippedWord is greater than 5. If it is add it to listOfWords

#return listOfWords at the end of readInWords method

slownik = {"the": 500, "door": 100}
oceny = {"religia": [6,6,6], "matematyka": [5,5]}

oceny['polski'] = [3,3,3]
print oceny['religia']
print oceny.get('polsk', 1)

print oceny.keys()
print oceny.values()



#print oceny

def countLetters(word):
    letterDict = {}

    for letter in word:
        if letter not in letterDict.keys():
            letterDict[letter] = 1
        else:
            letterDict[letter] += 1

    return letterDict

print countLetters("tytan")









