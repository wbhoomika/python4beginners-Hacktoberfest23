s=''
print("Enter multiple sentences:")
while True:
    line=input()
    if line:
        s=s+line+ '\n'
    else:
        break
print("Sentences entered here")
print(s)

while True:     
    print("1.Count words")
    print("2.To count number of characters including spaces and puntuations")
    print("3.To count number of words starting with t")
    print("4.Exit")
    c=int(input("Enter choice:"))

    if c==1:
        w=0
        for i in range(0,len(s)):
               if s[i]==' 'or s[i]=='\n':
                      w=w+1
               elif s[i]=='.' and s[i+1]!='\n' and s[i+1]!=' ':
                      w=w+1
        print("Words",w)

    elif c==2:
         ch=0
         for i in s:
               if i!='\n':
                   ch=ch+1
         print("Characters ",ch)

    elif c==3:
         count=0
         for  i in range(0,len(s)):
               if i==0 and (s[i]=='t'or s[i]=='T'):
                  count=count+1
               elif(s[i]==''or s[i]=='.')and (s[i+1]=='t' or s[i+1]=='T'):
                  count=count+1
               elif(s[i]=='\n'and i!=(len(s)-1)and (s[i+1]=='t' or s[i+1]=='T')):
                   count=count+1                           

         print("No of words starting with t:",count)

    elif c==4:
        exit()
    else:
        print("Wrong entry")
                    