#guess the number
def main():
    g_lim = 5; 
    g_number  = input("what to guess ")
    g_num = int(g_number);
    while(g_lim > 0):
        in1 = input("input ")
        val = int(in1)
        if(val == g_num):
            print("Bingo")
            break
        elif(val > g_num):
            print("try smaller")
        else:
            print("try bigger");
        g_lim -= 1
        print(f"only {g_lim} moves remaining")
    
main();
