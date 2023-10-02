import math as m
import random as r
  
# function to generate OTP 
def OTPgen() : 
  
    # Declare a string variable   
    # which stores all alpha-numeric characters 
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    varlen= len(string) 
    for i in range(6) : 
        OTP += string[m.floor(r.random() * varlen)] 
  
    return (OTP) 
  
# main function 
if __name__ == "__main__" : 
      
    print("Your One Time Password is ", OTPgen())
