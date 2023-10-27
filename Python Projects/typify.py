import time
from spellchecker import SpellChecker
t1=time.time()
inp=input(">>")
t2=time.time()
c=w=0
for i in list(inp.split()):
    w+=1
for i in inp:
    c+=1
t=(t2-t1)

def check_spelling(text):
    spell = SpellChecker()
    words = text.split()
    array = spell.unknown(words)
    global m
    global a
    global l
    m=0
    l=[]
    for i in array:
        l.append(i)
        m+=1
    a=(100-((m/w)*100))
check_spelling(inp)
print("Words typed : ",w)
print("Characters  : ",c)
print("Time elapsed: ",round(t,3))
print("Accuracy    : ",str(round(a,3))+"%")
print("Speed (wpm) : ",round(w/(t/60),3))
print("Speed (wps) : ",round(w/t,3))
print("Speed (cpm) : ",round(c/(t/60),3))
print("Speed (cps) : ",round(c/t,3))
if a!=100:
    print("Misspelled  : ", l)
