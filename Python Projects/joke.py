import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
]

def tell_joke():
    # Select a random joke from the list
    joke = random.choice(jokes)
    return joke

if __name__ == "__main__":
    while True:
        input("Press Enter to hear a joke...")
        joke = tell_joke()
        print(joke)
        cont = input("Do you want to hear another joke? (yes/no): ")
        if cont.lower() != "yes":
            print("Goodbye!")
            break
