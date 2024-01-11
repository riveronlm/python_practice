

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


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = [] 

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11  in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
        
    return sum(hand)
      
    
    
    