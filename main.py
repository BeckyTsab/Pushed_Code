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

def choosehouse():
    house = ''
    while house != '1' and house != '2':
            print('Which house will you go into? (1 or 2)')
            house = input()
    return house


def checkhouse(chosenhouse):
    print('You approach the house...')
    time.sleep(2)
    print('The door creeked open. You are inside...')
    time.sleep(3)
    print('The door slams behind you! In the dark...')
    print()
    time.sleep(2)
    friendlyhouse = random.randint(1, 2)

    if chosenhouse == str(friendlyhouse):
        print ('You find food and water. You are safe!') 
    else:
        print('You see the outline of a women in old Hmong attire \n crawling towards you. You are dead!')


displayIntro()
houseNumber = choosehouse()
checkhouse(houseNumber)

print("Thanks for playing")