import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # Randomly chooses a word from the list.
    while "-" in word or " " in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed

    lives = 6

    # Getting user iput
    while len(word_letters) > 0 and lives > 0:
        # Letters used.
        print("You have", lives, "lives left and you have already used these letters", " ".join(used_letters))

        # What the current word is (ie W_ _E)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 # Takes away one life.
                print("Oops! You letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")

        else:
            print("Invalid Character! Please try again.")

    # Here the word_letters == 0
    if lives == 0:
        print("Oopsy doopsy! You died :,)")
    else:
        print("My man! You have done it!")

hangman()