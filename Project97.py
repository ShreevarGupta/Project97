import random

print("Number guessing game")
r = random.randint(1, 9)
chances = 0
print("Guess a number between 1 to 9, you have 5 chances:")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if(guess == r):
        print("Congrats! You guessed it right!")
    elif(guess < r):
        print("You guessed the number less than the actual number.")
    else:
        print("The number is to large.")
    chances = chances+1

if not chances<5:
    print("You lose!")