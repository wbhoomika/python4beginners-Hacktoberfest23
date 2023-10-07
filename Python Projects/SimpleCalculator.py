def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result: ", add(num1, num2))
        elif choice == "2":
            print("Result: ", subtract(num1, num2))
        elif choice == "3":
            print("Result: ", multiply(num1, num2))
        elif choice == "4":
            print("Result: ", divide(num1, num2))
    else:
        print("Invalid Input")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        print("Thank you for using the calculator. Goodbye!")
        break
