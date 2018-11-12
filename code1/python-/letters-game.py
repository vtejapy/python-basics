# LETTERGAME
# Pick a random word from a list
# Let's us guess a letter of the word and show the position of the letter in the word

import random

word_list = ["carrot", "apple", "cucumber"]

# main function
def lettergame():
    #takes a random word from the list
    word = random.choice(word_list)
    print(word)
    print(len(word))

# Run lettergame
lettergame()
