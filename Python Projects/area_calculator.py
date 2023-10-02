import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_trapezoid_area(base1,base2,vertical_height):
    return 0.5*(base1+base2)*vertical_height

def calculate_ellipse_area(major_axis_radius,minor_axis_radius):
    return math.pi*major_axis_radius*minor_axis_radius

def calculate_square_area(length):
    return length * length


while True:
    print("Select a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Trapezoid")
    print("5. Ellipse")
    print("6. Square")
    print("7. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

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
        base1 = float(input("Enter the first base value of the trapezoid : "))
        base2 = float(input("Enter the second base value of the trapezoid : "))
        height = float(input("Enter the value of the vertical height : "))
        print(f"The area of the trapezoid is : {calculate_trapezoid_area(base1,base2,height)}")
    elif choice == "5":
        min_r = float(input("Enter the value of the radius of the minor axis : "))
        max_r = float(input("Enter the value of the radius of the major axis : "))
        print(f"The area of the ellipse is : {calculate_ellipse_area(max_r,min_r)}")
    elif choice == "6":
        side = float(input("Enter the side of the Square: "))
        area = calculate_square_area(side)
        print(f"The area of the square is: {area}")
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print ("Select a valid shape")