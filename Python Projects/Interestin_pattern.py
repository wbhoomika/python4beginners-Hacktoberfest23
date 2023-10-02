n = int(input("Enter the Rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')

    for k in range(2 * i - 1):
        if k % 2 == 0:
            print(i, end='')
        else:
            print("*", end='')

    for j in range(n - i):
        print(" ", end='')

    print()
