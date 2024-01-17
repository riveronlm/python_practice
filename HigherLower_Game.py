
import random
from art import hl,vs
from game_data import data

def select_keys(account):
    '''Formats data into selected keys.'''
    account_name = account["name"]
    acount_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {acount_descr}, from {account_country}"

#display art
print(hl)

#Genearte a random account form the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {select_keys(account_a)}")
print(vs)
print(f"Compare B: {select_keys(account_b)}")    

# Ask user for a guess.
input("Who has more followers? Type 'A' or 'B': ").lower()
#Check if user is correct.
## Get follower count of each account.

## Use if statement to check if user is correct.

#Give user feedback on their guess.

#Score keeping.

# Make the game repeatable. 

# Making acount at position B become the next account at position A.

# Clear the screen betwen rounds.

    
    
