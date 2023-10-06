import os

# Initialize an empty list to store tasks
tasks = []

# Function to add a new task to the list
def add_task(task):
    tasks.append({"task": task, "completed": False})

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_task_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to save tasks to a file
def save_tasks(filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")
        print("Tasks saved to", filename)

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task, completed = line.strip().split(",")
                tasks.append({"task": task, "completed": completed == "True"})
        print("Tasks loaded from", filename)
    else:
        print("File not found. Starting with an empty task list.")

# Main function
def main():
    filename = "tasks.txt"
    load_tasks(filename)

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Save Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            list_tasks()
            index = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(index)
        elif choice == '4':
            save_tasks(filename)
        elif choice == '5':
            save_tasks(filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
