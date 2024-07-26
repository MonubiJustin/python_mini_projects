import random
from database import data 
import os
from gameLogo import *

print(logo)
score = 0

def display(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}.'


def check_answer(guess, followers_count1, followers_count2):
    if followers_count1 > followers_count2:
        if guess == 1:
            return True
        else:
            return False
    else:
        if guess == 1:
            return False
        else:
            return True    
account_2 = random.choice(data)
game_over = False
while not game_over:
    account_1 = account_2
    account_2 = random.choice(data)
    while account_1 == account_2:
        account_2 = random.choice(data)

    print(f'Compare 1 : {display(account_1)}')
    print('\t\t',vs)
    print(f'Compare 2 : {display(account_2)}')

    followers_count1 = account_1['follower_count']
    followers_count2 = account_2['follower_count']

    guess = int(input("Who has more followers? '1' or '2' : "))
    is_correct = check_answer(guess, followers_count1, followers_count2)
    os.system('cls')
    print(logo)
    if is_correct:
        score += 1
        print(f'You are right. Your score is {score}')
    else:
        print(f'You are wrong...Your final score is {score}')
        game_over = True