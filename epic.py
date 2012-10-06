#My first game of rock, paper and scissors!
#Made by Jonathon Fuller
#If I could set this as a function, I could set the variables within the function as userChoice and computerChoice
#and I could set a limit, or infinate, based on user input. I also need to return a wrong entry with 'Please re-enter 
#your choice!'

import random

__author__ = 'jonathonfuller'
beginGame = input('Do you want to play rock, paper, scissors?')
# if beginGame is not re.match('a-z'):
    # print('Only use letters please!')

def gameOne(userChoice):
    computerChoice = random.random()
    if computerChoice < .34:
        computerChoice =  'rock'
    elif computerChoice >=.34 and computerChoice < .64:
        computerChoice =  'scissors'
    else:
        computerChoice = 'paper'
    if userChoice == computerChoice:
        return print('It is a tie!')
    if userChoice == 'scissors':
        if computerChoice == 'rock':
            print('The computer has won!')
        else:
            print('You have won!')
    if userChoice == 'paper':
        if computerChoice == 'rock':
            print('You have won!')
        else:
            print('The computer has won!')
    if userChoice == 'rock':
        if computerChoice == 'scissors':
            print('You have won!')
        else:
            print('The computer has won!')
if not beginGame != 'yes' or 'Yes' or 'YES':
    gameOne(input('Do you choose rock, paper, or scissors?'))
else:
    print('Okay! Goodbye!')
