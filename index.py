import random

print("Number guessing game")

number = random.randint(1,9)
chances = 0

print("Guess the number between 1 to 9:")

while chances < 5:
    guess=int(input())

    if guess == number:
        print("CONGRATULATIONS You WON!!!!!")
        break
    elif guess < number:
        print("The number is too low, Guess the number higher then", guess)
    else:
        print("The number is too high, Guess the number lower then", guess)

    chances += 1

if not chances < 5:
    print("YOU LOSE!!!!! The number is", number)