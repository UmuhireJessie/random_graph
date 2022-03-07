"""THIS PROGRAM IS GOING TO BE ABOUT ROLLING A DIE AND GIVING YOU A RANDOM 
NUMBER AS THE USER ROLL THE DIE AND ASK THE USER IF HE OR SHE WANTS TO PLAY 
AGAIN. """

import random

print("\nWelcome to the Program designed while waiting \n")

def rolling_die(min, max):
    while True:
        number = random.randint(min, max)
        print(f' You got: {number}')
        ask = input(" Do you want to play again? ")
        
        if ask == 'yes' or ask == 'y' or ask == 'yeah':
            continue
        else:
            print(" Thank you playing!! See you again.")
            break
    
                 
rolling_die(1, 6)

