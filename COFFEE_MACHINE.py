Menu = {
    'espresso': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 13
        },
        'cost': 250
    },
    'cappuccino': {
        'ingredients': {
            'water': 300,
            'milk': 100,
            'coffee': 23
        },
        'cost': 150
    },
    'latte': {
        'ingredients': {
            'water': 250,
            'milk': 200,
            'coffee': 34
        },
        'cost': 1300
    }
}

resources = {
    'water': 2000,
    'milk': 1500,
    'coffee': 150
}

profit = 0

def display_report():
    print(f"Water = {resources['water']}ml")    
    print(f"Milk = {resources['milk']}ml")    
    print(f"Coffee = {resources['coffee']}g")    
    print(f"Profit = ksh{profit}")

def check_resources(drink_resources):
    insufficient_items = []
    for item in drink_resources:
        if drink_resources[item] > resources[item]:
            insufficient_items.append(item)
    
    if insufficient_items:
        for item in insufficient_items:
            print(f"Sorry, insufficient {item}.")
        return False
    return True   

def make_payment():
    print('Please make your payment')
    total = int(input('Enter the amount in ksh: '))
    return total

def process_payment(payment_made, drink_cost):
    if payment_made >= drink_cost:
        global profit
        profit += drink_cost
        change = payment_made - drink_cost
        if payment_made != drink_cost:
            print(f'Here is your change off ksh{change}')
        return True    
    else:
        print('Sorry, Insufficient funds. here is your refund')  
        return False      

def make_coffee(drink_ingredients, chosen_drink):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f'Here is your {chosen_drink}. Enjoy!!!')    

is_off = False
while not is_off:
    choice = input("Which coffee drink would you like to purchase? (espresso/cappuccino/latte). ").lower()
    if choice == 'off':
        is_off = True
    elif choice == 'report':
        display_report()
    else:
        drink = Menu[choice]
        if check_resources(drink['ingredients']):
            payment_made = make_payment()  
            if process_payment(payment_made, drink['cost']):
                make_coffee(drink['ingredients'], choice)  