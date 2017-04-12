#this is an example of method that takes a number as an argument
#initializes new variable somethingToReturn and sets it's value to numer + 1 and then returns it

def simpleAddOne(number):
    somethingToReturn = number + 1
    return somethingToReturn

# based on that write:

#1:a method that takes a number as an argument and multiplies it by 2
def MultiplyByTwo(number):
    multiply= number*2
    return multiply


#2:a method that takes 2 arguments: number and byWhat and returns numer multiplied byWhat
def NumberByWhat(number, ByWhat):
    multiplyThem= number*ByWhat
    return multiplyThem

#3:a method that takes 3 arguments and returns their sum
def SumOfThree(number1,number2, number3):
    TheSum=number1+number2+number3
    return TheSum
#4:a method that takes a list as an argument and returns first element of that list
def FrstElemOfLst(rdmLst):
    rdmLst=[]
    FrstElem = rdmLst[0]
    return FrstElem

#5:a method that takes a list as an argument and returns last element of that list
def LastElemOfLst(rdmLst):
    rdmLst=[]
    LastElem = rdmLst[-1]
    return LastElem

#Na przecwiczenie if/else: (kilka linii, nie kombinujcie)

#a method that takes a string and checks if string is not empty("").
# If it's not - returns that string all in upper letters. Returns False otherwise.
def EmptyString(str):
    if str != " ":
        return str.upper()
    else:
        return False


#a method that takes a list and checks if this list is not empty([]).
# If it's not - returns first element of this list. Returns False otherwise.
def EmptyLst(lst):
    if lst != [()]:
        return lst[0]
    else:
        return False


#a method that takes a list and checks if this list has lenght of 5(len(lst) == 5).
# If len is 5 - returns that list without first and last element. Returns False otherwise.
def LstLong(lst):
    if len(lst)==5:
        return lst.pop[0,-1]
    else:
        return False
#a method that takes a number as an argument and checks if it has type of float (type(number) == float).
# If number is float - returns that number converted to int. Returns 0 otherwise.
def TypeOfFloat(number):
    if type(number)== float:
        return number.type(int)
    else:
        return "0"


