from random import *

#generate a random number
secret_number = randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#initalise the number of guesses
number_of_guesses = 0

#main game loop

while True:
    #increase the number of guesses
    number_of_guesses += 1
    
    #get the user's guess
    guess = int(input("Make a guess:"))

    #check the user's guess
    if guess < secret_number:
        print("Guess is too low, try again.")
    elif guess > secret_number:
        print("Guess is too high, try again.")
    else:
        print("Well done you've guessed the number!, it took you", number_of_guesses, "tries")
        break
    
