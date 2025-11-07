import random
from words import word_list  

word_list = ["python", "variable", "function", "loop", "module", "string"]


def word_guess_game():
    word = random.choice(word_list)
    guessed = "_" * len(word)
    guessed_letters = []

    print("Welcome to the Word Guess Game!")
    print(guessed)

    while "_" in guessed:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
            guessed = "".join([letter if letter in guessed_letters else "_" for letter in word])
        else:
            print("Incorrect guess.")
            guessed_letters.append(guess)
        print(guessed)

    print(f"Congratulations! You guessed the word '{word}'!")

if __name__ == "__main__":
    word_guess_game()

# Program using 'not in' operator
# word = input("Enter a word: ")

# if "a" not in word:
#     print("Your word does not contain the letter 'a'.")
# else:
#     print("Your word contains the letter 'a'.")
