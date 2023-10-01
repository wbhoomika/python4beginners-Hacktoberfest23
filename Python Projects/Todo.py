tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)

def list_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

while True:
    print("Options:")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        list_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
