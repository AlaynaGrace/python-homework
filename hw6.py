import math
import random


def count(char,text, c=0):  #Added c=0 to keep count
    if text == '':  #if the text is a null string just return what c is
        return c
    elif text[0] == char[0]:    #if the first part of text is the same as the character, return the function with the count + 1
        return count(char,text[1:],c+1)
    else:   #Otherwise, try again and keep the count the same
        return count(char,text[1:],c)

def isEqual(list1,list2):
    if len(list1) == len(list2):    #only will test it if the lengths are the same
        if list1 == [] and list2 == []: #if they are both null then they are the same
            return True

        elif list1[0] == list2[0]:  #if the first terms are the same it will return the function
            return isEqual(list1[1:],list2[1:])
            
        else:
            return False
            
    else:
        return False

def convertBase(n,base,remainder=''):   #Put remainder in to keep track of the remainders without it resetting every time
    a = n//base
    b = a%base
    if n // base == 0:  #Want it to stop when the quotient is 0
        r = str(n%base) #want to add up the remainders but in string form
        remainder += r  #add the remainder to the string
        return remainder
    elif n%base == 10:  #The entire alphabet corresponding with certain remainders
        remainder = str(b)+'A'
        return remainder
    elif n%base == 11:
        remainder = str(b)+'B'
        return remainder
    elif n%base == 12:
        remainder = str(b)+'C'
        return remainder
    elif n%base == 13:
        remainder = str(b)+'D'
        return remainder
    elif n%base == 14:
        remainder = str(b)+'E'
        return remainder
    elif n%base == 15:
        remainder = str(b)+'F'
        return remainder
    elif n%base == 16:
        remainder = str(b)+'G'
        return remainder
    elif n%base == 17:
        remainder = str(b)+'H'
        return remainder
    elif n%base == 18:
        remainder = str(b)+'I'
        return remainder
    elif n%base == 19:
        remainder = str(b)+'J'
        return remainder
    elif n%base == 20:
        remainder = str(b)+'K'
        return remainder
    elif n%base == 21:
        remainder = str(b)+'L'
        return remainder
    elif n%base == 22:
        remainder = str(b)+'M'
        return remainder
    elif n%base == 23:
        remainder = str(b)+'N'
        return remainder
    elif n%base == 24:
        remainder = str(b)+'O'
        return remainder
    elif n%base == 25:
        remainder = str(b)+'P'
        return remainder
    elif n%base == 26:
        remainder = str(b)+'Q'
        return remainder
    elif n%base == 27:
        remainder = str(b)+'R'
        return remainder
    elif n%base == 28:
        remainder = str(b)+'S'
        return remainder
    elif n%base == 29:
        remainder = str(b)+'T'
        return remainder
    elif n%base == 30:
        remainder = str(b)+'U'
        return remainder
    elif n%base == 31:
        remainder = str(b)+'V'
        return remainder
    elif n%base == 32:
        remainder = str(b)+'W'
        return remainder
    elif n%base == 33:
        remainder = str(b)+'X'
        return remainder
    elif n%base == 34:
        remainder = str(b)+'Y'
        return remainder
    elif n%base == 35:
        remainder = str(b)+'Z'
        return remainder
    else:   #if the quotient is not 0, continue testing the function until it is or it is part of the alphabet
        a = n//base
        r = str(n%base)
        remainder += r
        return convertBase(a,base,remainder)
