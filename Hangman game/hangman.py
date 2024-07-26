import random
from hangman_stages import *

print('Lets play hangman!!')
print('You have only 6 lives so try to guess the word within 6 attempts! Goodluck!!')

word_bank = ['justin', 'monubi', 'michelle', 'bosibori']
chosen_word = random.choice(word_bank)

# generating as many blanks as letters in the chosen word
blank = []
for i in chosen_word:
    blank += '_'
print(blank)
lives = 6  # setting the lives required before death
game_over = False  # control variable for changing/quiting/exiting the while loop
while not game_over:
    guessed_letter = input('Guess a letter: ').lower()
    # iterating through the chosen word to fetch the index of the letters
    for position in range(len(chosen_word)):
        letter = chosen_word[position]   # assigning the letter to the variable based on the index, the starting point being at 0
        if guessed_letter == letter:  # checking if guessed letter is equal to the first iterated letter
            blank[position] = letter  # if true, replace '_' in blanks with the letter at that position

   # letter comes here if it ain't in chosen word
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True  # exiting the loop
            print('You lose!')
        print(f'You guessed {guessed_letter} that is not present in the word. So you lose a life')
    print(blank)
    if '_' not in blank:
        game_over = True   # exiting the loop
        print('You win')
    print(stages[lives])
