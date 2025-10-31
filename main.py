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

words = ["Sky", "Ground", "Space", "Groundhog", "Fire"]
rWords = random.choice(words)

name = input("Please enter your name: ")

gLetters = ''
choices = 10

while choices > 0:
    guess = input("Enter the letters for the unknown word")
    if guess == rWords:
        

