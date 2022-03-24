#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
difficulty_level = input("Choose a Difficulty. Type 'easy' or 'hard': ")

attempts = 0
if difficulty_level == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts to guess the number.")
elif difficulty_level == 'hard':
    attempts = 5
    print(f"You have {attempts} attempts to guess the number.")
else:
    print("Invalid Choice!\nGame Ends.")

import random
computer = random.randint(1,101)

while(attempts!=0):
    guess = int(input("Make a guess : "))
    if guess == computer:
        print(f"You got it! The answer was {computer}.")
        break;
    elif guess<computer:
        print("Too low.\nGuess again.")
        attempts -= 1
        print(f"You've {attempts} attempts remaining to guess the number.")
    else:
        print("Too High.\nGuess again.")
        attempts -= 1
        print(f"You've {attempts} attempts remaining to guess the number.")
else:
    print("You've run out of guesses, you lose.")
    print(f"The correct answer is {computer}")