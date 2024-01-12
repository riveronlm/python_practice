

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import blackjack_logo
import os

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    '''Deals a card randomly.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    '''Takes a list of cards and returns the score.'''
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)    
    return sum(hand)

def compare(user_score,computer_score):
    ''' Compares the players hand to see who wins.'''
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "BlackJack! computer wins!"
    elif user_score == 0 :
        return "BlackJack! you win.!"
    elif user_score > 21:
        return "You went over, You lose!"
    elif computer_score > 21:
        return "Computer went over, You win!"
    elif user_score > computer_score:
        return "You win! " 
    else:
        return "The computer wins!"    
        
def play_game():
    
    print(blackjack_logo)
                        
    user_cards = []
    computer_cards = []
    is_game_over = False 

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0  or computer_score == 0 or user_score > 21 :
            is_game_over = True
        else:
            user_move = input("Do you want to draw another card. TYPE 'y' or 'n'. ")
            if user_move == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)             

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")           
    print(compare(user_score,computer_score)) 

while   input("Do you wnat to pay a game of BlackJack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
 
      
    
    
    