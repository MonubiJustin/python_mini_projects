import os


# defining the calculations functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

# dictionary containing functions
operations_symbols = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calc():
    num1 = float(input('Enter first number: '))

    # iterating through the dictionary to display the keys
    for i in operations_symbols:
        print(i)
    game_over = False
    while not game_over:    
        sign = input('Pick a sign: ')    
        num2 = float(input('Enter next number: '))

        # fetching the operator sign inorder to access the function
        calculator_function = operations_symbols[sign]
        output = calculator_function(num1, num2)
        print(f'{num1} {sign} {num2} = {output}')
        continue_flag = input(f"Type 'y' to continue with {output}, type 'n' to start a new calculation and 'x' to quit.: \t").lower()
        if continue_flag == 'y':
            num1 = output
        # using the recursion method
        elif continue_flag == 'n':
            game_over = True
            os.system('cls') 
            calc()    
        else:
            game_over = True
            print('\n Goodbyeee!!!')       


calc()            