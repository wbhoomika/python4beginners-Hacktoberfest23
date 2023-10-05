import random

def guess_the_number():
    # Generate a random number between 1 and 100
    r = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            n = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if n == r:
            print(f"Congratulations! You guessed the correct number {n} in {attempts} attempts.")
            break
        elif n > r:
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")

if __name__ == "__main__":
    guess_the_number()
