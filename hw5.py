import math

somelist = [[45,-99],[24,83],[-48, -68],[-97,99],[-8,-77],[-2, 50],
            [44,41],[-48,-58],[-1,53],[14,86],[31,94],[12,-91],[33,50],
            [82,72],[83,-90],[10,78],[7,-22],[90,-88],[-21,5],[6,23]]

    
def shortestDist(alist):
    smallDist = []  #null list where distances are going to go
    for i in range(len(alist)):    
        if i != len(alist)-1:   #we don't want i==len(alist) because len(alist)+1 is too large
            x = alist[i][0]
            y = alist[i][1]

            a = alist[i + 1][0]
            b = alist[i + 1][1]
            

            distance = math.sqrt((a-x)**2+(b-y)**2) #distance equation
        smallDist += [distance] #add distances to smallDist list

    return min(smallDist)   #find the minimum of that list and return it

def unitTest():
            
    somelist = [[45,-99],[24,83],[-48, -68],[-97,99],[-8,-77],[-2, 50],
                [44,41],[-48,-58],[-1,53],[14,86],[31,94],[12,-91],[33,50],
                [82,72],[83,-90],[10,78],[7,-22],[90,-88],[-21,5],[6,23]]

    return shortestDist(somelist)  #Doesn't work????



def gameState(tttGame):
    i=0
    while i<=2 and i != 3:
        if tttGame[i][0] == tttGame[i][1] and tttGame[i][1] == tttGame[i][2]:
            print(tttGame[i][1])#Checks if the rows are the same
            i = 3
        elif tttGame[0][0] == tttGame[1][1] and tttGame[1][1] == tttGame[2][2]:
            print(tttGame[0][0])    #Checks if the left to right diagonal is all the same
            i = 3
        elif tttGame[0][2] == tttGame[1][1] and tttGame[1][1] == tttGame[2][0]:
            print(tttGame[0][2])    #Checks if the right to left diag is all the same
            i = 3
        elif tttGame[0][i] == tttGame[1][i] and tttGame[1][i] == tttGame[2][i]:
            print(tttGame[0][i])    #Checls if the columns are the same
            i = 3
        elif tttGame[0][i] != '' and tttGame[1][i] != '' and tttGame[2][i] != '':
            print('D')  #If nothing matches and there are no null strings, it is a draw
            i = 3
        else:
            i += 1
            if i == 2:
                print('')
def testTTT():
    a = [['X','','O'],['X','O',''],['X','','O']]    #X should win   
    b = [['O','','X'],['X','O',''],['X','','O']]    #O should win
    c = [['O','X','O'],['X','X','O'],['X','O','X']] #Draw
    d = [['','X','O'],['X','O',''],['X','','O']]    #No win or draw

    gameState(a)
    print('X wins')
    
    gameState(b)
    print('O wins')
    
    gameState(c)
    print('Draw')
    
    gameState(d)
    print('No win, no draw')
    
