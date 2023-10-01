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
    else:
        print ("Select a valid shape")
    print ("%.2f" % area)