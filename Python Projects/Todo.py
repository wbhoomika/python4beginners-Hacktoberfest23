import json

# Function to load the to-do list from a file
def load_todo_list(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save the to-do list to a file
def save_todo_list(todo_list, filename):
    with open(filename, 'w') as file:
        json.dump(todo_list, file)

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})

# Function to view tasks
def view_tasks(todo_list):
    for index, task in enumerate(todo_list, start=1):
        status = " [X] " if task["completed"] else " [ ] "
        print(f"{index}.{status} {task['task']}")

# Main program loop
def main():
    filename = "todo.json"
    todo_list = load_todo_list(filename)

    while True:
        print("\nTodo List:")
        view_tasks(todo_list)
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            add_task(todo_list, task)
            save_todo_list(todo_list, filename)
        elif choice == "2":
            index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= index < len(todo_list):
                todo_list[index]["completed"] = True
                save_todo_list(todo_list, filename)
        elif choice == "3":
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(todo_list):
                del todo_list[index]
                save_todo_list(todo_list, filename)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
