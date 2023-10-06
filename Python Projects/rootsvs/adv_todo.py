import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Function to add a new task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove the selected task from the list
def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        save_tasks()
    except IndexError:
        pass

# Function to save tasks to a text file
def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Create the main window
root = tk.Tk()
root.title("Advanced To-Do List")

# Create and pack widgets
task_entry = tk.Entry(root, width=50)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Load tasks from a text file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.insert(tk.END, line.strip())
except FileNotFoundError:
    pass

# Pack widgets
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
task_list.pack()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the main loop
root.mainloop()
