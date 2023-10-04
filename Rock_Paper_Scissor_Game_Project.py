import random
from playsound import playsound



#  Rock Paper Scissors

def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose r
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True
    
    # Check for all possibilities when computer chose p
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True

print("Computer's Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3) 

if randNo == 1:
        comp = 'r'
elif randNo == 2:
        comp = 'p'
elif randNo == 3:
        comp = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")


            
playsound('C:\\Users\\hp\\Desktop\\Konark\\Python Practise\\game.mp3')