import random

def choose_word():
    words = ["python", "java", "ruby", "javascript", "html", "css"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect guess! {attempts} attempts remaining.")
        else:
            print("Correct guess!")

        displayed = display_word(word, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Congratulations! You guessed the word.")
            break

    if "_" in displayed:
        print(f"Sorry, you're out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
