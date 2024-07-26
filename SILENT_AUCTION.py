import os

print('*******Welcome to the Silent Auction Program*********')

def highest_bidder(bidder_data):
    highest_bidder = 0
    winner = ''
    for bidder in bidder_data:
        bid_amount = bidder_data[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of {highest_bidder}')
    print(bidder_data)

bidder_info = {}

game_over = False
while not game_over:
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))
    bidder_info[name] = bid
    other_bidders = input("Are there any other bidders?'yes' or 'no' : ").lower()
    if other_bidders == 'yes':
        os.system('cls')
    elif other_bidders == 'no':
        game_over = True
        os.system('cls')
        highest_bidder(bidder_data=bidder_info)
    