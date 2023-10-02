def areacalculator():
    input = input("Enter the shape you want to calculate area of: ")
    area = 0
    pie = 3.14
    if input == "Square":
        side = int(input("Enter the value of side: "))
        area = area + (side ** 2)
    elif input == "Circle":
        radius = int(input("Enter the value of radius: "))
        area = area + (2 * pie * radius)
    elif input == "Rectangle":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of length: "))
        area = area + (length * width)
    elif input == "Triangle":
        base = int(input("Enter the value of base: "))
        height = int(input("Enter the value of height: "))
        area = area +(0.5 * base * height)

import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side*side
while True:
    print("Select a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Square")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    elif choice == '2':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {area}")
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    elif choice == '4':
        side = float(input("Enter the side of the Square: "))
        area = calculate_square_area(side)
        print(f"The area of the square is: {area}")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print ("Select a valid shape")
    print ("%.2f" % area)