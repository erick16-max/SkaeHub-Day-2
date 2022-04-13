#Create a Python project to guess a number that has randomly been selected.
import random




guessed_number = int(input("Guess the Number:"))

random_number = random.randrange(0,101)
def guess_check ():
    return guessed_number == random_number
if guess_check():
    print (f"Hooray! The random number {random_number} is equal to the guessed number {guessed_number}")
else:
    print( f"random number {random_number} is not equal to your guess {guessed_number}, Please try again")
       


    
        

