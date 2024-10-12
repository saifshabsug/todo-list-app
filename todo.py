import tkinter as tk
from tkinter import messagebox
import os

# Initialize the main app window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# List to store tasks
tasks = []

# Function to update the Listbox with current tasks
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as completed (strikethrough style)
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index] = "✔ " + tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

# Function to save tasks to a text file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Save Confirmation", "Tasks saved to tasks.txt")

# Function to load tasks from the file on startup
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for task in f:
                tasks.append(task.strip())
        update_task_list()

# Entry widget for task input
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons for task actions
add_task_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text="Mark as Completed", width=20, command=mark_task_completed)
mark_task_button.pack(pady=5)

save_tasks_button = tk.Button(root, text="Save Tasks", width=20, command=save_tasks)
save_tasks_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, height=10, width=40, font=("Arial", 14))
task_listbox.pack(pady=10)

# Load tasks on startup
load_tasks()

# Start the Tkinter event loop
root.mainloop()