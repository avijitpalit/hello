import tkinter as tk
from tkinter import simpledialog

# Create the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window as we only want the dialog

# Prompt the user for input
user_input = simpledialog.askstring("Input", "Please enter your name:")

# Check if input was provided and print it
if user_input is not None:
    print(f"Hello, {user_input}!")
else:
    print("No input provided.")