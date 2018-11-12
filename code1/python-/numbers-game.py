# NUMBERS GAME
# Author: Bram Pauwelyn

from random import randint

# Generate a random number
random_number = randint(0, 100)
i = 0

# Asks the user to guess the number
print("Guess a number between 0 and 100")


# Checks if number is correct
while i < 10:
    guess = input('> ')
        # IF number is correct, congratulations
    if guess == random_number:
        print("congratulations")
        break

    # Else number is smaller
    elif guess < random_number:
        print("You have to guess higher")
        i += 1
        continue

    # Else
    else:
        print("You have to guess lower")
        continue
        i += 1
