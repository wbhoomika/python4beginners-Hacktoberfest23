def bmi_range(bmi):
    if bmi <= 18.5:
        print("You are Underweight\n")
    elif bmi <= 24.9:
        print("You are in the Normal Weight range\n")
    elif bmi <= 29.9:
        print("You are Overweight\n")
    else:
        print("You are Obese\n")

def us_units():
    weight_lb = float(input("Enter your weight in Pounds: "))
    height_in = float(input("Enter your height in Inches: "))
    bmi = 703 * (weight_lb / (height_in)**2)
    print("\nYour BMI is:", bmi)
    bmi_range(bmi)

def metric_units():
    weight_kg = float(input("Enter your weight in Kilograms: "))
    height_cm = float(input("Enter your height in Centimeters: "))
    bmi = (weight_kg / (height_cm/100)**2)
    print("\nYour BMI is:", bmi)
    bmi_range(bmi)


print("1. Imperial/US Units")
print("2. Metric Units")
unit_sys = int(input("Please Enter your preferred Unit System [1 or 2]: "))
print("")
if unit_sys == 1:
    us_units()
elif unit_sys == 2:
    metric_units()
else:
    print("Please Enter a valid Input [1 or 2]!")




    