import tkinter as tk

# Function to add a task
def add_task():
    task = task_entry.get()  # Get the task from the entry field
    if task:  # If the task is not empty
        task_listbox.insert(tk.END, task)  # Add it to the listbox
        task_entry.delete(0, tk.END)  # Clear the entry field

# Function to remove the selected task
def remove_task():
    selected_task = task_listbox.curselection()  # Get the selected task
    if selected_task:  # If a task is selected
        task_listbox.delete(selected_task)  # Remove it from the listbox

# Create the main window
root = tk.Tk()
root.title("Simple To-Do List")

# Instruction Label
instructions = tk.Label(root, text="1. Enter a task and click 'Add Task'.\n"
                                    "2. Select a task and click 'Remove Task' to delete it.", pady=10)
instructions.pack()

# Entry field for tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Buttons to add and remove tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()