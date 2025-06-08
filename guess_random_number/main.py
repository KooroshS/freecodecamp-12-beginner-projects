""" We want to create a game in which the computer has a random number
 and we try to guess it."""

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low. Guess again!")
        elif guess > random_number:
            print("Too high. Guess again!")
    
    print("Congrats, you got it!!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # low or high are the same. No difference which
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay, the computer has guess your number, {guess}, correctly!!")


computer_guess(1000)