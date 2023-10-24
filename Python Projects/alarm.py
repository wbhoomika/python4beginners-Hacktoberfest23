import datetime
import time

def set_specific_alarm():
    try:
        alarm_time = input("Enter the time for the alarm (HH:MM AM/PM): ")
        alarm_time = datetime.datetime.strptime(alarm_time, '%I:%M %p')
        return alarm_time
    except ValueError:
        print("Invalid time format! Please use HH:MM AM/PM.")
        return set_specific_alarm()

def set_relative_alarm():
    try:
        relative_time = int(input("Enter the number of minutes from now for the alarm: "))
        if relative_time < 0:
            print("Please enter a positive number.")
            return set_relative_alarm()
        return datetime.datetime.now() + datetime.timedelta(minutes=relative_time)
    except ValueError:
        print("Invalid input! Please enter a number of minutes.")
        return set_relative_alarm()

def main():
    print("Welcome to the Alarm Clock program!")
    
    while True:
        print("\nChoose an option:")
        print("1. Set a specific time for the alarm")
        print("2. Set a relative time for the alarm")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            alarm_time = set_specific_alarm()
            break
        elif choice == '2':
            alarm_time = set_relative_alarm()
            break
        elif choice == '3':
            print("Exiting the program.")
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    while datetime.datetime.now() < alarm_time:
        time.sleep(1)

    print("\nALARM!!!")

if __name__ == "__main__":
    main()
