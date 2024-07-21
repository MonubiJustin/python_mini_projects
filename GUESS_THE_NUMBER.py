import random
print('Let me think of a number between 1 to 50')

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def check_level(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS

def check_answer(guess, answer, attempts):
    if guess > answer:
        print('Your guess is too high')
        return attempts - 1
    elif guess < answer:
        print('Your guess is too low')
        return attempts - 1
    else:
        print(f"Your guess is right...The answer was {answer}")    
        return

def game():
    answer = random.randint(1, 50)
    print(answer)
    level = input("Choose level of difficulty...Type 'easy' or 'hard' : ").lower()
    attempts = check_level(level_chosen=level)

    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts to guess the number")
        guess = int(input("Make a Guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You are out of guesses...You lose!")
            return
        elif guess != answer:
            print('Guess again')

game()