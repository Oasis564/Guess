"""
Requirement: Make a guess the word game
Plan:
    step 1: Get the list of words we choose from
    step 2: Randomize them
    step 3: Create the lives and mistake variables
    step 4: Check if the letters chosen for the randomized words are correct, if not then reduce their lives by -1
    step 5: if letter has been guessed, make the remaining letters be hidden until guessed correctlyy for each and every single one of them
    step 6: Put them into a loop so the player can keep inputting
    step 7: Print whether or not they got the word correct or if they lost all their lives.
"""

import random

words = ["sky", "ground", "space", "groundhog", "fire"]
random_word = random.choice(words)

name = input("=Please enter your name=: ")

guessed_letters = ''
choices = 10

print(random_word)

def contains_letter(s: str) -> bool:
    """Return True if the string contains at least one letter (Unicode-aware)."""
    return any(ch.isalpha() for ch in s)

class SmartString(str):
    def contains(self, sub: str) -> bool:
        return sub in self

while choices > 0:
    guess = input("=Enter the letters for the unknown word=: ")
    guessed_letters = f"{guessed_letters}{guess}"
    # Show the letters if guessed corectly and not show them if not guessed correctly
    for i in range(len(random_word)):
        # I need to compare if the current letter of the word is present inside the guessed letter
        
        if random_word[i] in guessed_letters:
            print(random_word[i])
        else:
            print("-")
            
    # Now we have to make the lives and mistakes so there is a form of punishment for not getting it correctly.
    
    if guess in random_word:
        print("You have gotten the correct letter!")
    else:
        choices = choices-1
        print("You have gotten the letter wrong, you have ", choices, " lives remaining...")
        if choices == 0:
            print("You have lost, ", name, "!")
            break
    if guessed_letters == random_word:
        print("Good job", name, "! You have won the game!!!")
        break
    