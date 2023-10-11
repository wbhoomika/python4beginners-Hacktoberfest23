import random

def guess():
    num = random.randrange(1, 10)
    while True:
        user = int(input("Guess a number: "))
        if num == user:
            return "Congratulations! You guessed it right!"
        elif num > user:
            print("Too low")
        elif num < user:
            print("Too high")
        else:
            print("Invalid input")


print(guess())
