import random
class Card():   #Class that sets a value and a suit for a card
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    def getValue(self): #Use to see the value
        return self.__value

    def getSuit(self):  #Use to see the suit
        return self.__suit

    def __str__(self):  #Prints in form of: Value of Suit
        return str(self.__value) + ' ' +'of' + ' ' + str(self.__suit)


class Carddeck():
    def __init__(self,index=0):
        self._deck = ['Ace of Diamonds', 'Ace of Hearts', 'Ace of Spades',
                       'Ace of Clubs','2 of Diamonds', '2 of Hearts',
                       '2 of Spades', '2 of Clubs','3 of Diamonds', '3 of Hearts',
                       '3 of Spades', '3 of Clubs','4 of Diamonds', '4 of Hearts',
                       '4 of Spades', '4 of Clubs','5 of Diamonds', '5 of Hearts',
                       '5 of Spades', '5 of Clubs','6 of Diamonds', '6 of Hearts',
                       '6 of Spades', '6 of Clubs','7 of Diamonds', '7 of Hearts',
                       '7 of Spades', '7 of Clubs','8 of Diamonds', '8 of Hearts',
                       '8 of Spades', '8 of Clubs','9 of Diamonds', '9 of Hearts',
                       '9 of Spades', '9 of Clubs','10 of Diamonds', '10 of Hearts',
                       '10 of Spades', '10 of Clubs','Jack of Diamonds',
                       'Jack of Hearts','Jack of Spades', 'Jack of Clubs',
                       'Queen of Diamonds', 'Queen of Hearts', 'Queen of Spades',
                       'Queen of Clubs','King of Diamonds', 'King of Hearts',
                       'King of Spades', 'King of Clubs','Ace of Diamonds', 'Ace of Hearts', 'Ace of Spades',
                       'Ace of Clubs','2 of Diamonds', '2 of Hearts',
                       '2 of Spades', '2 of Clubs','3 of Diamonds', '3 of Hearts',
                       '3 of Spades', '3 of Clubs','4 of Diamonds', '4 of Hearts',
                       '4 of Spades', '4 of Clubs','5 of Diamonds', '5 of Hearts',
                       '5 of Spades', '5 of Clubs','6 of Diamonds', '6 of Hearts',
                       '6 of Spades', '6 of Clubs','7 of Diamonds', '7 of Hearts',
                       '7 of Spades', '7 of Clubs','8 of Diamonds', '8 of Hearts',
                       '8 of Spades', '8 of Clubs','9 of Diamonds', '9 of Hearts',
                       '9 of Spades', '9 of Clubs','10 of Diamonds', '10 of Hearts',
                       '10 of Spades', '10 of Clubs','Jack of Diamonds',
                       'Jack of Hearts','Jack of Spades', 'Jack of Clubs',
                       'Queen of Diamonds', 'Queen of Hearts', 'Queen of Spades',
                       'Queen of Clubs','King of Diamonds', 'King of Hearts',
                       'King of Spades', 'King of Clubs','Ace of Diamonds', 'Ace of Hearts', 'Ace of Spades',
                       'Ace of Clubs','2 of Diamonds', '2 of Hearts',
                       '2 of Spades', '2 of Clubs','3 of Diamonds', '3 of Hearts',
                       '3 of Spades', '3 of Clubs','4 of Diamonds', '4 of Hearts',
                       '4 of Spades', '4 of Clubs','5 of Diamonds', '5 of Hearts',
                       '5 of Spades', '5 of Clubs','6 of Diamonds', '6 of Hearts',
                       '6 of Spades', '6 of Clubs','7 of Diamonds', '7 of Hearts',
                       '7 of Spades', '7 of Clubs','8 of Diamonds', '8 of Hearts',
                       '8 of Spades', '8 of Clubs','9 of Diamonds', '9 of Hearts',
                       '9 of Spades', '9 of Clubs','10 of Diamonds', '10 of Hearts',
                       '10 of Spades', '10 of Clubs','Jack of Diamonds',
                       'Jack of Hearts','Jack of Spades', 'Jack of Clubs',
                       'Queen of Diamonds', 'Queen of Hearts', 'Queen of Spades',
                       'Queen of Clubs','King of Diamonds', 'King of Hearts',
                       'King of Spades', 'King of Clubs','Ace of Diamonds', 'Ace of Hearts', 'Ace of Spades',
                       'Ace of Clubs', '2 of Diamonds', '2 of Hearts',
                       '2 of Spades', '2 of Clubs','3 of Diamonds', '3 of Hearts',
                       '3 of Spades', '3 of Clubs','4 of Diamonds', '4 of Hearts',
                       '4 of Spades', '4 of Clubs','5 of Diamonds', '5 of Hearts',
                       '5 of Spades', '5 of Clubs','6 of Diamonds', '6 of Hearts',
                       '6 of Spades', '6 of Clubs','7 of Diamonds', '7 of Hearts',
                       '7 of Spades', '7 of Clubs','8 of Diamonds', '8 of Hearts',
                       '8 of Spades', '8 of Clubs','9 of Diamonds', '9 of Hearts',
                       '9 of Spades', '9 of Clubs','10 of Diamonds', '10 of Hearts',
                       '10 of Spades', '10 of Clubs','Jack of Diamonds',
                       'Jack of Hearts','Jack of Spades', 'Jack of Clubs',
                       'Queen of Diamonds', 'Queen of Hearts', 'Queen of Spades',
                       'Queen of Clubs','King of Diamonds', 'King of Hearts',
                       'King of Spades', 'King of Clubs']
        self._index = index

    def __repr__(self): #Shows deck as a string
        return str(self._deck)

    def shuffle(self):  #Shuffles the deck and makes the index 0
        random.shuffle(self._deck)
        self._index = 0

    def dealcard(self): #Deals the next card in the deck
        self._index += 1
        if self._index == 52:
            return self._deck[self._index-1], random.shuffle(self._deck)#Shuffles if it is the last card
        elif self._index < 51:
            return self._deck[self._index-1]
        else:
            self._index = 0 #Starts index over
            return self._deck[self._index]

class Pokerhand(Carddeck):  #Pokerhand is a child of Carddeck
        def __init__(self):
            super().__init__()  #Inherit everything from init
            self.__five = ['Ace of Spades','2 of Diamonds','10 of Diamonds',
                           'Jack of Clubs', 'King of Spades']   #Random starting hand
            
        def newHand(self):  #Shuffles the deck and creates a new hand of cards
            random.shuffle(self._deck)
            self.__five = []
            for i in range(5):
                self.__five += [self._deck[i]]

        def __repr__(self): #Prints the list of cards as a string
            return str(self.__five)

        def rank(self): #Ranks the cards depending on the type of hand it deals
            r = {}
            nVal = []
            nSuit = []
            vs = []
            for i in range(len(self.__five)):
                if self.__five[i][0] in '23456789AJQK':
                    nVal += self.__five[i][0]   #Taking all the values and put all of them into a list
                    if self.__five[i][0] == 'A':
                        nSuit += self.__five[i][7]  #Taking all of the suits and putting them in a list
                        total = self.__five[i][0] + self.__five[i][7]
                        vs += [total]   #Put the value and suit together and put them in a list too
                    elif self.__five[i][0] == 'J':
                        nSuit += self.__five[i][8]
                        total = self.__five[i][0] + self.__five[i][8]
                        vs += [total]
                    elif self.__five[i][0] == 'Q':
                        nSuit += self.__five[i][9]
                        total = self.__five[i][0] + self.__five[i][9]
                        vs += [total]
                    elif self.__five[i][0] == 'K':
                        nSuit += self.__five[i][8]
                        total = self.__five[i][0] + self.__five[i][8]
                        vs += [total]
                    else:
                        nSuit += self.__five[i][5]
                        total = self.__five[i][0] + self.__five[i][5]
                        vs += [total]
                else:   #Used for 10
                    nVal += [self.__five[i][0] + self.__five[i][1]]
                    nSuit += self.__five[i][6]
                    total = self.__five[i][0] + self.__five[i][1]+self.__five[i][6]
                    vs += [total]
            s = {}  #Dictionary to count the suits
            v = {}  #Dictionary to count the values
            for i in range(len(vs)):    #Put everything in one big dictionary
                if vs[i] in r:
                    r[vs[i]] += 1
                else:
                    r[vs[i]] = 1
            for i in range(len(vs)):    #Put all the suits in one dictionary
                if vs[i][1] in s:
                    s[vs[i][1]] += 1
                else:
                    s[vs[i][1]] = 1
            for i in range(len(vs)):    #Put all the values in another dictionary
                if vs[i][0] in v:
                    v[vs[i][0]] += 1
                else:
                    v[vs[i][0]] = 1
            
            ind = []    #List to index the values dictionary
            for thing in v:
                ind += [thing]

            if len(v) == 5: #If there are 5 cards...
                count = 0
                nVal.sort()
                t = [['2','3','4','5','A'],['2','3','4','5','6'],
                    ['3','4','5','6','7'],['4','5','6','7','8'],
                    ['5','6','7','8','9'],['10','6','7','8','9'],
                    ['10','7','8','9','J'],['10','8','9','J','Q'],
                    ['10','9','J','K','Q']]
                for j in range(8):
                    for i in range(4):
                        if t[j][i] == nVal[i]:  #Check if they match one of the lists above after they have been sorted
                            count += 1
                        else:
                            count = 0
                if count == 5:  #If everything matches...
                    if len(s) == 1: #..and it only has one suit
                        return 8 #It's a straight flush!
                    else:
                        return 4 #Otherwise it is just a straight
                elif len(s) == 1:   #If it is all one suit but does not match any of the ordered lists
                    return 5 #It's a flush!
                else:
                    return 0    #If there are five cards but nothing matches then it is a high card
            elif len(v) == 4:   #If there are only four values...
                return 1 #Then there must be at least one match! It's a pair!

            elif len(v) == 3: #If there are only three values..
                return 2    #There must be two pairs!

            elif len(v) == 2:   #If there are only three values...
                if v[ind[0]] == 4 or v[ind[1]] == 4: #...and the first or second thing have the same value
                    return 7 #Then it is a four of a kind!
                elif v[ind[0]] == 3 and v[ind[1]] == 2: #Otherwise if it has two values total but 3 and 2 cards of the same value
                    return 6    #Then it's a full house!
                elif v[ind[1]] == 2 and v[ind[0]] == 3:
                    return 6
                elif v[ind[0]] == 3 or v[ind[1]] == 3:  #If it only has three of a kind
                    return 3    #Then it is three of a kind!

                    
                
def main():
    carddeck = Carddeck()
    p = Pokerhand()
    ranks = {'High Card': 0, 'One Pair': 0, 'Two Pair': 0,'Three of a Kind': 0,
             'Straight': 0, 'Flush': 0, 'Full House': 0, 'Four of a Kind': 0,
             'Straight Flush': 0}
    rankList = []
    for i in range(100000): #This loop creates new hands and ranks them, then takes the ranks and adds them to the dictionary
        p.newHand()
        n = p.rank()
        if n == 0:
            b = 'High Card'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 1:
            b = 'One Pair'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 2:
            b = 'Two Pair'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 3:
            b = 'Three of a Kind'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 4:
            b = 'Straight'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 5:
            b = 'Flush'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 6:
            b = 'Full House'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 7:
            b = 'Four of a Kind'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
        elif n == 8:
            b = 'Straight Flush'
            ranks[b] += 1
            p.newHand()
            n = p.rank()
    for c in ranks: #Then it adds each of the numbers to a list so that list can be sorted
        rankList += [ranks[c]]
    rankList.sort()
    for i in rankList:  #The new list is used so that it can create an order of least frequent to most frequent hand
        for thing in ranks:
            if ranks[thing] == i:
                print(thing, ':', i)

                
    
    
        

    
