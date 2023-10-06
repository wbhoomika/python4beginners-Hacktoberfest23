import os

def display_menu():
    print("Text Editor Menu:")
    print("1. Open a file")
    print("2. Create a new file")
    print("3. Edit the current file")
    print("4. Save the current file")
    print("5. Quit")

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""

def create_file(filename):
    with open(filename, 'w') as file:
        pass

def edit_file(content):
    print("Editing the file. Enter your text (press Enter to save and exit):")
    new_content = []
    while True:
        line = input()
        if not line:
            break
        new_content.append(line)
    content = '\n'.join(new_content)
    return content

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print(f"File '{filename}' saved.")

if __name__ == '__main__':
    current_filename = None
    current_content = ""
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the file name to open: ")
            current_content = open_file(filename)
            current_filename = filename
            print(current_content)

        elif choice == '2':
            filename = input("Enter the new file name to create: ")
            create_file(filename)
            current_content = ""
            current_filename = filename
            print(f"File '{filename}' created.")

        elif choice == '3':
            if current_filename:
                current_content = edit_file(current_content)
            else:
                print("No file is currently open. Please open or create a file first.")

        elif choice == '4':
            if current_filename:
                save_file(current_filename, current_content)
            else:
                print("No file is currently open. Please open or create a file first.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a valid option.")
