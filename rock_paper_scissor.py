# rock paper scissor
import random
user = input('Enter rock , paper or scissor:\n').lower()
options = ['rock', 'paper', 'scissor']
computer = random.choice(options)
if user not in options:
    print('Invalid input, you loose')
else:
    print(f'Computer inputed {computer}')
    if user == computer:
        print('It\'s a draw')
    elif computer == 'paper' and user == 'rock':
        print('You lose')
    elif computer == 'scissor' and user == 'paper':
        print('You lose')
    elif computer == 'rock' and user == 'scissor':
        print('You lose')
    else:
        print('You win')



