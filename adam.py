#ADAM

import random
answers = ['Did you try turning it off and on?', 'Blame Networking.', 'Have you tried Googling the error?', 
           'Try reading the documentation.', 'Take a short break and try again.', 
           'Get some coffee and try again.', 'Maybe you\'re hungry? Take a break.', 'Try meditation.', 
           'Unplug the machine.','Delete everything on the machine.', 'Wipe the hard drive.', 
           'Find an open window and throw the machine out of it.', 'It works better hacked',
           'Sorry, I\'m on vacation in Flavortown right now.', 'Security isn\'t that important, don\'t worry.'
           'I know it hasn\'t worked yet, but if you try 10 or more times it might work', 
           'Please open up a ticket and forward it to Dr. Cole', 
           'Go to the bathroom, create a giant wad of toilet paper and scream all of your worries into it at the top of your lungs.',
           'Adam is not here to answer your question but his consulting fees start at $200 an hour.',
           'Sorry, my ability to help you is commensurate with your experience.',
           'Flavortown is near.', 'It\'s "Bomgar", not "Bombguard"',
           'Let me run this up the flagpole to management and see what they think.',
           'Waiting for leadership...', 'I don\'t have any cycles left to solve that problem.']

print('\nHello, I am A.D.A.M., The Automated Disaster Answering Machine.')

def Magic8Ball():
    print('\nAsk me a question.\n')
    print('> ', end='')
    input()
    print ('\n' + answers[random.randint(0, len(answers)-1)] + '\n')
    Replay()
    
def Replay():
    print ('Do you have another question? [Y/N] ', end='')
    reply = input()
    if reply == 'Y' or reply == 'y':
        Magic8Ball()
    elif reply == 'N' or reply == 'n':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()

		
Magic8Ball()
