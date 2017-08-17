import random
def guessingGame(player1, player2):
    answer = random.randint(0,100)
    while(True):
        i = 0
        while i < 1:
            print(player1.getName()+"'s turn to guess: ", end ="")
            f1guess = player1.getGuess()
            if checkForWin(player1,f1guess,answer):
                return
            print(player2.getName()+"'s turn to guess: ", end= "")
            f2guess = player2.getGuess()
            if checkForWin(player2,f2guess,answer):
                return
            p1guess = f1guess
            p2guess = f2guess
            i = 1
        
        print(player1.getName()+"'s turn to guess: ", end ="")
        guess = player1.getBetterGuess(answer,p1guess)
        p1guess = guess
        if checkForWin(player1,guess,answer):
            return
        print(player2.getName()+"'s turn to guess: ", end= "")
        guess = player2.getBetterGuess(answer,p2guess)
        p2guess = guess
        if checkForWin(player2,guess,answer):
            return
    
def checkForWin(player,guess,answer):
    print(player.getName(),"guesses",guess)
    if answer == guess:
        print("You're right! You win!")
        return True
    elif answer < guess:
        print("Your guess is too high.")
    else:
        print("Your guess is too low")
    return
class Player():
    def __init__(self,name = ''):
        self._name = name
    def getName(self):
        return self._name
    def getGuess(self):
        return 0
    def getBetterGuess(self,answer,guess):
        guess = int(input("Your guess: "))
        return guess
class HumanPlayer(Player):
    def __init__(self,name=''):
        super().__init__()
        self._name = name

    def getGuess(self):
        guess = int(input('Your guess: '))
        return guess

class ComputerPlayer(Player,):
    def __init__(self,name='Computer'):
        super().__init__()
        self._name = name
    def getGuess(self):
        guess = random.randint(0,100)
        return guess
    def getBetterGuess(self,answer,pguess):
        if pguess < answer:
            guess = random.randint(pguess+1,100)
            return guess
        else:
            guess = random.randint(0,pguess-1)
            return guess
        

def main():
    p1 = str(input('Is player 1 a computer or human?: '))
    p2 = str(input('Is player 2 a computer or human?: '))
    p1 = p1.lower()
    p2 = p2.lower()
    if p1 == 'computer' and p2 == 'computer':
        player1 = ComputerPlayer()
        player2 = ComputerPlayer()
        guessingGame(player1,player2)
    elif p1 == 'computer' and p2 == 'human':
        name = str(input('Enter your name: '))
        player1 = HumanPlayer(name)
        player2 = ComputerPlayer()
        guessingGame(player2,player1)
    elif p1 == 'human' and p2 == 'computer':
        name = str(input('Enter your name: '))
        player1 = HumanPlayer(name)
        player2 = ComputerPlayer()
        guessingGame(player1,player2)
    else:
        name1 = str(input('Enter name of player 1: '))
        name2 = str(input('Enter name of player 2: '))
        player1 = HumanPlayer(name1)
        player2 = HumanPlayer(name2)
        guessingGame(player1,player2)
        
