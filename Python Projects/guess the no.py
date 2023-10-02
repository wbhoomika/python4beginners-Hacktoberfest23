import random

r=random.randint(0,100)

while(1):
    n=int(input("enter the guess:"))
    if(n==r):
        print("Congratulations you guess correct:",n)
        break
    if(n>r):
       print("guess is high......... Try again")
    else:
        print("guess is low..........Try again")