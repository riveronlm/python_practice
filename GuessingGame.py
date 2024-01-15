############### Number Guessing Game ###############

import random
from art import guess

EASY_LEVEL = 10
HARD_LEVEL = 5



def compare(the_answer, player_guess,turns):
    ''' Checks user guess against actual answer.'''
    if player_guess > the_answer:
        print("Too high! Try a lower number.")
        return turns -1
    if player_guess < the_answer:
        print("Too low! Try a higher number.")
        return turns -1
    else:
        print(f"Good guess! The number is: {the_answer}")
         
def sets_difficulty():
    level = input(" Choosee a difficulty. Type 'easy' or 'hard: ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
def guess_counter(total_guess):
    '''Keeps tracks of how many guesses are left.'''
    if total_guess > 0:
        total_guess -= 1
        return f"Guesses remaining: {total_guess}"
    
    else:
        return "Your ran out of guesses! Good luck next time" 
def game():
    print(guess)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    the_answer = random.randint(1,100)
    
    turns = sets_difficulty()
    
    player_guess = 0 
    while guess != the_answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        player_guess = int(input("Make a guess: "))
        
        turns = compare(the_answer,player_guess,turns)
        if turns == 0:
            print("You ran out of guesses, you lose.")
            return    
        elif guess != the_answer:
            print("Guess again.")
            
game()            



  
    
    


           
       