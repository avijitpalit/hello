import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox

class InputDialog(ThemedTk):
    def __init__(self):
        super().__init__()

        self.title("Input Form")
        self.geometry("300x150")

        # Apply a theme
        self.set_theme("arc")  # "arc" is a modern theme, you can choose another one

        # Create and place widgets
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill='both', expand=True)

        self.label1 = ttk.Label(frame, text="First Input:")
        self.label1.grid(row=0, column=0, sticky='w', pady=5)
        self.first_input = ttk.Entry(frame)
        self.first_input.grid(row=0, column=1, pady=5, sticky='ew')

        self.label2 = ttk.Label(frame, text="Second Input:")
        self.label2.grid(row=1, column=0, sticky='w', pady=5)
        self.second_input = ttk.Entry(frame)
        self.second_input.grid(row=1, column=1, pady=5, sticky='ew')

        button_frame = ttk.Frame(self)
        button_frame.pack(side='bottom', pady=10)

        self.submit_button = ttk.Button(button_frame, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.grid_columnconfigure(1, weight=1)

    def submit(self):
        first_input = self.first_input.get()
        second_input = self.second_input.get()
        messagebox.showinfo("Inputs", f"First Input: {first_input}\nSecond Input: {second_input}")

if __name__ == "__main__":
    app = InputDialog()
    app.mainloop()
