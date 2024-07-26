from letter_bank import *


def shiftKey(text, key):
    changed_text = ''
    for i in text:
        if i in alphabets:
            position = alphabets.index(i)
            new_position = (position + key) % 26
            changed_text += alphabets[new_position]
        else:
            changed_text += i
    return changed_text


game_over = False
while not game_over:
    method = input("Type 'encrypt' for encryption, type 'decrypt' for decryption.\n").lower()
    text = input('Enter your message:\n')
    shift_key = int(input('Enter shift key:\n'))
    if method == 'encrypt':
        encryption = shiftKey(text, shift_key)
        print(f'Here is the text after encryption: {encryption}')
    elif method == 'decrypt':
        decryption = shiftKey(text, -shift_key)
        print(f'Here is the text after decryption: {decryption}')
    Continue_flag = input("Type 'yes' to continue, otherwise type 'no'\n").lower()
    if Continue_flag == 'no':
        game_over = True
        print('Goodbye,,Have a nice day!!!!')

