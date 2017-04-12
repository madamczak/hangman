# AD1
# a)
def multipleBy(li):
    zwrot = li * 2
    return zwrot
# b
def multipleByWhat(li,ByWhat):
    zwrotB = li * ByWhat
    return zwrotB

# c
def sumOfArguments(arg1,arg2,arg3):
    Suma = arg1+arg2+arg3
    return Suma

# d
def takeListAndRetElement(list):
    list = [1,2,3,4,5,6]
    return list[0:]

# e
def takeListAndRetLastElement(list2):
    list2 = [1,1,1,1,1,2,2,2,3,3,3,5,4,4,5,4,87]
    element = len(list2)

    return element

# Ad2
# a
def checkStr(str):
    if str is not "":
        return upper.str()
    else: False

# b
def checkLst(lst):
    if lst is not []:
        return lst[0:]
    else: False

# c
def checkLstLen(lst2):
    if len(lst2)==5:
        return lst2[1:3]
    else: False

# d
def checkNumType(number):
    if type(number) == float:
        number = number.type(int)
        return number
    else:
        0