#Name: Becky Chang
#Date: 08/02/23
#Dr. Plowcha
#CIS 245-T303


import random
import time

def displayIntro():
	print('''Lost deep in the forest, you are in a place you don't know. 
    In front of you, there are two houses. In one house, a safe haven. 
    The other house has a bloodhungry spirit lurking and there is no way out.''')
	print()

def chooseCave():
    cave = ''
    #It looks like the indentation of the next line is not correct. 
    # Deleting one space before 'while' on the next line would fix that:
    while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
#Looks like there is a name error for caves, try: cave
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else: #Looks like the parentheses the print call is missing. You need 
        #to do the following:  print('Gobbles you down in one bite!') 
        print ('Gobbles you down in one bite!') 


displayIntro()
#It looks like there is a name error for choosecave(), try: chooseCave().
caveNumber = chooseCave()
checkCave(caveNumber)

#There seems to be a grammatical error here, change the word planing to: playing    
print("Thanks for playing")