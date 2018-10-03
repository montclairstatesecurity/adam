#ADAM

from __future__ import print_function
from builtins import input
import random
import os

answers = ['Did you try turning it off and on?', 'Blame Networking.', 'Have you tried Googling the error code?', 
           'Try reading the documentation.', 'Take a short break and try again.', 
           'Get some coffee and try again.', 'Maybe you\'re hungry? Take a break.', 'Try meditation.', 
           'Unplug the machine.','Delete everything on the machine.', 'Wipe the hard drive.', 
           'Find an open window and throw the machine out of it.', 'It works better hacked.',
           'Sorry, I\'m on vacation in Flavortown right now.', 'Security isn\'t that important, don\'t worry.',
           'I know it hasn\'t worked yet, but if you try 10 or more times it might work', 
           'Please open up a ticket and forward it to the president', 
           'Go to the bathroom, create a giant wad of toilet paper and scream all of your worries into it at the top of your lungs.',
           'Sorry, my ability to help you is commensurate with your experience.',
           'Flavortown is near.', 'It\'s "Bomgar", not "Bombguard"',
           'Let me run this up the flagpole to management and see what they think.',
           'Waiting for leadership...', 'I don\'t have any cycles left to solve that problem.',
           'Restart the domain controllers']

_=os.system("cls")
_=os.system("clear")

def ADAM():
    print('\nHello, I am A.D.A.M., The Automated Disaster Answering Machine.')
    print('\nAsk me a question.\n')
    print('> ', end='')
    input()
    print ('\n' + answers[random.randint(0, len(answers)-1)] + '\n')
    Replay()
    
def Replay():
    print ('Do you have another question? [Y/N] ', end='')
    reply = input()
    if reply == 'Y' or reply == 'y':
	_=os.system("cls")
        _=os.system("clear")
        ADAM()
    elif reply == 'N' or reply == 'n':
        exit()
    else:
        print('My apologies, I did not catch that. Please try again.')
        Replay()

		
ADAM()
