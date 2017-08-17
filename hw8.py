def reverseAssoc(dictionary):   #Put in a dictionary and get the reverse dictionary
    new = {}    #New and empty dictionary
    for i in dictionary:
        new[dictionary[i]] = i #Add everything at point i and associate it with i
    print(new)
        
def getNumber():
    alphabet = {'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3',
                'g':'4','h':'4','i':'4','j':'5','k':'5','l':'5',
                'm':'6','n':'6','o':'6','p':'7','q':'7','r':'7',
                's':'7','t':'8','u':'8','v':'8','w':'9','x':'9',
                'y':'9','z':'9'}    #phone alphabet 
    number = 0
    while number != '':     #Loop continues until user just presses enter
        number = str(input('Enter a telephone number: '))
        number = number.lower() #Makes everything lowercase, like the alphabet dictionary above
        new = ''    #Null string for making the number without any punctuation
        for ch in number:
            if ch not in '()-.#[]!,/_* ':   #Removes punctuation
                new += ch #Adds everything else to the new string

        newnumber = ''  #Final string needed for creating the phone number
        if len(new) == 10:  #If it has an area code/is 10 characters long
            for i in new:
                if i == new[2] or i == new[5]:  #If it is the 2nd or 5th thing, add a '-' after the number
                    if i in '1234567890':
                        newnumber += i
                        newnumber += '-'
                    else:
                        newnumber = newnumber + alphabet[i] + '-'
                elif i in '1234567890':  #If it is not the 2nd or 5th thing and it is a number, just add it to the new string
                    newnumber += i
                else:
                    newnumber += alphabet[i]    #If it is not the 2nd or 5th thing and it is not a number, change it into one using the dictionary
            print('Numeric telephone number:', newnumber)   #Print the new number
            print() #Create space between this try and the next one
        elif len(new) == 7: #Same thing as the case above but without the area code/is only 7 characters long
            for i in new:
                if i == new[2]:
                    if i in '1234567890':
                        newnumber += i
                        newnumber += '-'
                    else:
                        newnumber = newnumber + alphabet[i] + '-'
                elif i in '1234567890':  
                    newnumber += i
                else:
                    newnumber += alphabet[i]
            print('Numeric telephone number:', newnumber)
            print()
        elif number == '':  #Added this to make sure it doesnt just assume that by having a null string that it is an incorrect number
            print()
        else:   #If they enter a number that is the incorrect length, it will say it is invalid and have them try again
            print('Invalid number!')
            print()
