#My first game of rock, paper and scissors!
#Made by Jonathon Fuller
#If I could set this as a function, I could set the variables within the function as userChoice and computerChoice
#and I could set a limit, or infinate, based on user input. I also need to return a wrong entry with 'Please re-enter your #choice!'

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
print('The computer has chosen: ' + computerChoice)
if userChoice == computerChoice:
    print('It is a tie!')
    return tieRound
if userChoice = 'rock':
    if computerChoice = 'scissors':
         print('You win!')
    else:
         print('The computer has won!)
if userChoice = 'paper':
   if computerChoice = 'rock':
      print('You win!')
   else:
      print('The computer has won!')
if userChoice = 'scissors':
   if computerChoice = 'rock':
      print('The computer has won!')
   else:
      print ('You win!')
return secondRound

    