import random

letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd',
           'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h',
           'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
           'm', 'M', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
           's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
print('Welcome to the password generator')
l = int(input('How many letters would you like in your password?\n')) # 5
n = int(input('How many numbers would you like in your password?\n'))
s = int(input('How many symbols would you like in your password?\n'))

password_list = []
for i in range(l):
    password_list += random.choice(letters)
for i in range(n):
    password_list += random.choice(numbers)
for i in range(s):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ''
for i in password_list:
    password += i
print(f'\nYour password is: {password}')

