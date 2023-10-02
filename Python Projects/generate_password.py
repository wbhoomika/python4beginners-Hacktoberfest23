import random
passlen = int(input("enter the length of the password: "))
s = "aqwertyuiopasdfghjkl;zxcvbnm,./234567890-=/*-"
p = "".join(random.sample(s,passlen))
print(p) 
