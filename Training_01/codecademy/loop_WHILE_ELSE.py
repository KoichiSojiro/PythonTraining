'''
Created on Jul 14, 2016

@author: trannh08
'''
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print("The hidden number is:", random_number)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print ("You win!")
        break
    else:
        guesses_left -= 1
else:
    print ("You lose.")