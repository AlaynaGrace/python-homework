import math
import random
import turtle

def sdev():
    sdList=[]   #sdList is an empty list
    total = 0
    while True:
        n = float(input("Enter a number (enter 999 to quit): "))    #ask user to enter numbers and to stop type 999
        if n != 999:
            sdList += [n]   #add the number to the list
            total += 1  #add one to the total to keep track of the number of numbers
        else:
            avg = total / len(sdList)
            i = 0
            top = 0
            y = len(sdList)
            while i<len(sdList):
                a = sdList[i]
                numerator = (a - avg)**2
                top = top + numerator
                i += 1

            standDev = math.sqrt(top/y) #find the sqrt of the entire thing
            print('Standard Deviation:',standDev)
            False


def polyAdd(list1,list2):
    total = 0
    i = 0
    finalList = []
    while i<len(list1):
        total = list1[i] + list2[i] #add the two lists together, piece by piece so that the first parts add together, then the next parts add and so on
        finalList += [total]
        i += 1
    print(finalList)

def polyTest():
    a = [36,0,0,0,3]
    b = [0,0,0,72,-16]
    polyAdd(a,b)    #finds 36x**4+3 + 72x - 16
    
    c = [-5,32,-6]
    d = [10,12,6]
    polyAdd(c,d)    #finds -5x**2+32x-6+10x**2+12x+6

def subStringCount(substr,fullstr):
    i = 0
    word = ""   #word is an null string
    for ch in fullstr:
        if ch == " ": #if the character in the word is a space then...
            if word == substr:  #compare word to sub
                i += 1
            word = "" #reset word
        else:   #create word
            word += ch            
    print('The word appears',i,'many times.')
                    
def main():
    a = str(input('Enter a string: '))
    b = str(input('Enter a substring: '))
    subStringCount(b,a) #finds how many times the str b is in a
    
