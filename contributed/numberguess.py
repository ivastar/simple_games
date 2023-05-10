#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributed by Chandana Hedge, May 10, 2023
import random
import numpy as np

def generate_number():
    # ask user for lower and upper limits
    # or tell user what the limits are
    #generate the number
    
    ll = int(input("Give the lower limit:- "))
    ul = int(input("Give the uppter limit:- "))
    
    while ul < ll:
        ul = int(input(f"Give the uppter limit that is bigger than {ll}:- "))
    
    number = np.random.randint(low=ll, high=ul)
    #print(number)
    return number, ll, ul

def game(n, ll, ul):

    # limit number of guesses"?
    count = 5

    # there are smarter ways to determine number of guesses based on interval size

    n_guesses = 0

    while n_guesses < count:

        n_guesses += 1
        
        guess = int(input("Guess a number:- "))
        
        # here be dragons
        if guess == n:
            print("Congrats! You got us.")
            return None
        elif guess > n:
            print(f"Oops too high! Number should be in range: ({ll},{guess})")
            ul = guess
        else:
            print(f"Oops too low! Number should be in range: ({guess},{ul})")
            ll = guess
      
    
    print("Oh, too many tries...loser!")
        
        
if __name__ == '__main__':
    
    number, ll, ul = generate_number()
    game(number, ll, ul)
        
