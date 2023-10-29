""" python program for finding the factorial of a number """

import sys

def Factorial(num):
    mul=1
    for i in range(0,num):
        if num == 0:
            return 1
        else:
            mul = mul*(num-i)
    return mul
    
def get_input():
    for i in range(3,0,-1):                      
        num = input("enter a number:")
        if num.isnumeric():                    
            num = int(num)                      
            return num
        else:
            print("enter integer only")                    
            print(f'{i-1} chances are left' if (i-1)>1 else f'{i-1} chance is left') 
        continue   

if __name__ == '__main__':
    num = get_input()
    if type(num) is type(None):               
        print("Try again!")
        sys.exit()
    else:
        fact=Factorial(num)
        print(f'The factorial of {num} is {fact}')

