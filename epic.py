import random

__author__ = 'jonathonfuller'
print ('Hello world!')
userChoice = input('What do you choose? Rock, paper, or scissors?')
userChoice = str(userChoice)
computerChoice = random.random()
if computerChoice < .34:
    computerChoice =  'rock'
elif computerChoice >=.34 and computerChoice < .64:
    computerChoice =  'scissors'
else:
    computerChoice = 'paper'
if userChoice == computerChoice:
    print('It is a tie!')
    if userChoice = 'rock' and computerChoice = 'paper':
        print('The computer has won!')
    if userChoice = 'scissors' and computerChoice = 'paper':
        print('You have won!')
