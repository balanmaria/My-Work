import art
from replit import clear

print(art.logo)
print("Welcome to the secret auction program!")
bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for key in bidding_record:
        bid_amount=int(bidding_record[key])
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=key
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price=input("What is your bid? $")
    bids[name] = price
    answer=input("Are there any other bidders? Type 'yes' or 'no'.")
    if answer == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    else:
        clear()