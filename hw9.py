import turtle
from time import time

class Bug():
    def __init__(self,pos = 0): #Starts at the position given and turned to the right
        turtle.penup()
        self.__position = pos
        turtle.forward(pos)
        self.__direction = 1
        turtle.right(90)

    def move(self): #Will move the bug forward one step
        self.__position +=1
        turtle.forward(1)

    def turn(self): #Will turn the bug around so it is facing the left
        turtle.right(180)
        if self.__direction == 1:
            self.__direction = -1
        else:
            self.__direction = 1

    def display(self):  #displays the position and direction using numbers, words, and symbols
        d = ''
        for i in range(self.__position - 1):
            d += '.'
        if self.__direction == -1:
            d += '<'
            p = 'left'
        else:
            d += '>'
            p = 'right'
        
        print('position',self.__position,'direction',p,':','    ',d)
        
def testA():    #Makes a bug class and moves it forward once, turns it once and then moves it 13 more times while displaying its movements
    b = Bug(10)
    b.move()
    b.turn()
    for i in range(13):
        b.move()
        b.display()
    

class Stopwatch():
    
    def __init__(self,start = time(),end = time()): #start time and end time are equal to the actual time unless otherwise specified
        self.__startTime = start
        self.__endTime = end

    def getStartTime(self): #Shows the start time
        return self.__startTime

    def getEndTime(self):   #Shows the end time
        return self.__endTime

    def start(self):    #Resets start time to current time
        self.__startTime = time()

    def stop(self): #Resets end time to current time
        self.__endTime = time()

    def elapsedTime(self):  #Displays the amount of time that has elapsed
        counter = 0
        while time() != self.__endTime :
            elapsed = time() - self.__startTime
            print(elapsed)

def testB():    #Finds the time it takes to sort a list with 10,000 things in it
    sortMe = []
    for i in range(100):
        for j in range(100):
            sortMe += [j]
    a = Stopwatch(time(),time()+10000)
    a.elapsedTime()
    sortMe.sort()
    a.stop()
        
            
