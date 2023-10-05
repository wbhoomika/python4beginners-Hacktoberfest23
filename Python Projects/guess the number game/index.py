
import random
import sys

low = 1
high = 30
guesslimit = 5

print("Guess a number between {0} and {1}".format(low, high))
print("You have {0} guesses to get the right number".format(guesslimit))

guessnumb = 0
number = random.randint(low, high)

try:
	while guessnumb < guesslimit:
		try:
			guess = int(input('What\'s your guess? '))
		except ValueError:
			print("Couldn\'t convert input to Integer")
			continue
	
		if guess < low or guess > high:
			print("Value out of range ({0} - {1})".format(low, high))
		else:
			guessnumb += 1
			
			if guess < number:
				print("Your guess was too low")
		
			if guess > number:
				print("Your guess was too high")
		
			if guess == number:
				break
	
except KeyboardInterrupt:
	print("\n  ^C detected, terminating...")
	sys.exit()

except EOFError:
	print("\n  ^D detected, terminating...")
	sys.exit()

if guess == number:
	print("Great, you guessed the number in {0} trys".format(guessnumb))
else:
	print("No, I was thinking of the number {0}".format(number))
