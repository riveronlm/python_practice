
import random
from art import hl,vs,gameover
from game_data import data
import os

def clear():
    '''Cross-platform clear screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def select_keys(account):
    '''Formats data into selected keys.'''
    account_name = account["name"]
    acount_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {acount_descr}, from {account_country}"

def check_guess(guess, a_followers, b_followers):
    '''Compares which account has more followers
    and returns True if user guess right. Or False
    if they got it wrong.'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():   
    #display art
    print(hl)
    score = 0
    game_continues = True
    account_b = random.choice(data)

    while game_continues:
        #Genearte a random account form the game data.
        account_a = account_b
        account_b = random.choice(data)
        
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {select_keys(account_a)}")
        print(vs)
        print(f"Compare B: {select_keys(account_b)}")    

        # Ask user for a guess.
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        #Check if user is correct.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_guess(user_guess,a_follower_count,b_follower_count)
        #Give user feedback on their guess.
        
        clear()
        print(hl)
        
        if is_correct:
            score += 1
            print (f"Correct! Curent score: {score}")
        else:
            game_continues = False
            print(gameover)
            print(f"Wrong! Final score: {score}")
game()           
    
    
