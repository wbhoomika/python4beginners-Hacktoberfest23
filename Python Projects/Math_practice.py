import random


def main():
    j = 0
    k = 0
    level = get_level()
    while j < 10:
        i = 0
        X, Y = generate_integer(level)
        ans = X + Y
        while i < 3:
            print(X, "+", Y, "=", sep=" ", end=" ")
            sol = input()
            if str(sol) == str(ans):
                break
            else:
                print("EEE")
                i = i + 1
        if i == 3:
            print(X, "+", Y, "=", ans, sep=" ")
            k = k + 1
        j = j + 1
    print("Score:", 10 - k)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
        return X, Y
    lower = "10"
    upper = "99"
    # an attempt to make the limits more automated for future levels(>3)
    while level > 1:
        if len(lower) == int(level):
            X = random.randint(int(lower), int(upper))
            Y = random.randint(int(lower), int(upper))
            return X, Y
        lower = lower + "0"
        upper = upper + "9"


"""
     if level == 1:
        X = random.randint(0,9)
        Y = random.randint(0,9)
        return X,Y
     elif level == 2:
        X = random.randint(10,99)
        Y = random.randint(10,99)
        return X,Y
     else:
        X = random.randint(100,999)
        Y = random.randint(100,999)
        return X,Y
        """

if __name__ == "__main__":
    main()
