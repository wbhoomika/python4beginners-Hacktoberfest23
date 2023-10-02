import random

print(
    "There are 3 levels. You will be given 5 mathematical problems and will be given 3 chances to solve it."
)

# level 1 has single digit problems
# level 2 has double digit problems
# level 3 has triple digit problems
# the code is restricted to level 3 in get_level(). But it can be increased.


def main():
    j = 0
    k = 0
    number_of_problems = 5
    level = get_level()
    while j < number_of_problems:
        i = 0
        X, Y = generate_integer(level)
        problem, ans = get_problem(X, Y)
        while i < 3:  
            print(problem, end="")
            sol = input()
            if str(sol) == str(ans):
                break
            else:
                print("Wrong answer")
                i = i + 1
        if i == 3:
            print("The correct answer is\n", X, "+", Y, "=", ans, sep=" ")
            k = k + 1
        j = j + 1
    print(f"Score: {(number_of_problems - k)}/{number_of_problems}")


def get_problem(X, Y):
    operations = ["+", "-", "*"]
    operator = random.choice(operations)
    if operator == "+":
        ans = X + Y
        return f"{X} + {Y} = ", ans
    elif operator == "-":
        ans = X - Y
        return f"{X} - {Y} = ", ans
    else:
        ans = X * Y
        return f"{X} X {Y} = ", ans


def get_level():
    while True:
        try:
            level = int(input("Select a level[1,2,3]\nLevel: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                print("Level must be an integer: 1,2 or 3")
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


if __name__ == "__main__":
    main()
