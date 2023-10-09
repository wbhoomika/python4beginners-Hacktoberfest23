import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def cuboid_volume(length, width, height):
    return length * width * height

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

while True:
    print("Choose a shape to calculate its volume:")
    print("1. Sphere")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("Any other number to exit...")

    choice = int(input("Enter the number of your choice (1-4): "))

    if choice == 1:
        radius = float(input("Enter the radius of the sphere: "))
        result = sphere_volume(radius)
    elif choice == 2:
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        result = cuboid_volume(length, width, height)
    elif choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        result = cylinder_volume(radius, height)
    elif choice == 4:
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        result = cone_volume(radius, height)
    else:
        print("Exiting")
        break

    print(f"The volume of the selected shape is: {result:.2f}")

