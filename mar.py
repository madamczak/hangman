# def fuzzBizz3(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FuzzBizz"
#     elif number % 5 == 0:
#         return "Bizz"
#     elif number % 3 == 0:
#         return "Fuzz"
#     else:
#         return number
#
# print fuzzBizz3(4)

#==============================================================================================

# def fuzzBizz4(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FuzzBizz"
#     elif number % 5 == 0:
#         return "Bizz"
#     elif number % 3 == 0:
#         return "Fuzz"
#     else:
#         return number
#
# print fuzzBizz4(4)

#==============================================================================================

#method that sums elements in the list. Takes one argument - lstToSum
#initialize a variable sumValue and set it to 0.0
#loop through elements in the list and add each element to sumValue
#return sumValue

def sumOfListElements(lstToSum):
    sumValue=0.0

    for i in lstToSum:
        sumValue+=i     #+= dodawanie zmiennej w funkcji

    return sumValue

print sumOfListElements([1, 2, 3])



#==============================================================================================

#method that takes two arguments Aarg, and Barg which are integers and checks if their sum is greater than 0
#initialize variable sumOfAB and set it to the sum of Aarg and Barg
#check if it is greater than 0. If it is - return True
#if it's not - return False

def isSumPositive(Aarg,Barg):
    if Aarg+Barg>0:
        return True
    else:
        return False

print isSumPositive(0, -50)

#==============================================================================================

#method readInWords that takes a file path(to the file with words) as an argument and returns a list of words longer than 5 letters.
#initialize variable listOfWords and set it to empty list

#initailize variable fileWithWords and set it to the opened file
#initialize varialbe wordsFromFile and use readlines method to set it to the list of words from fileWithWords

#iterate over each word in wordsFromFile
#initialize variable strippedWord and set it to word without whitespaces (use strip method)
#check if length of strippedWord is greater than 5. If it is add it to listOfWords

#return listOfWords at the end of readInWords method