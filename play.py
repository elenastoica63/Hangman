def get_hello_message():
    name = input("Hello, What is your name? ")
    return input("Well, " + name.capitalize() + ", Let's play Hangman!")

print(get_hello_message())

import random
import countries_and_capitals_easy
import countries_and_capitals_medium
import countries_and_capitals_hard

def difficulties():
    difficulty = input("Choose a level - easy (maximum 7 letters and 7 lives), medium (Between 8-10 letters and 6 lives) or hard (11 letters or more and 5 lives)")
    while True:
        if difficulty == "easy":
            secretWord = random.choice(countries_and_capitals_easy)
            break
        elif difficulty == "medium"
            secretWord = random.choice(countries_and_capitals_medium)
            break
        else:
            secretWord = random.choice(countries_and_capitals_hard)
            break

def printGuessedLetter():
    attempts = (len(secretWord) + 2)
    print("Your Secret word is: " + ''.join(difficulties())
    for n in secretWord:
        difficulties.append('_')
    printGuessedLetter()

print("The number of allowed guesses for this word is:", attempts)

print(difficulties())