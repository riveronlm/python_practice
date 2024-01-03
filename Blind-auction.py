import os
clear = lambda:os.system('clear')

from art import logo 
print(logo)
print("Welcome to the secret auction program!")

bids = {}

name = input("What is your name?")
bid = input("Enter your bid. $")
bids[name] = bid
bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

