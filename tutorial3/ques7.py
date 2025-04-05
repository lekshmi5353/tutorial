import tkinter as tk
from tkinter import messagebox
import math

def compute_square_root():
    try:
        number = int(input_entry.get())
        if number < 0:
            raise ValueError("Negative number")
        result = math.sqrt(number)
        result_label.config(text=f"√{number} = {result:.2f}")
    except ValueError:
        messagebox.showerror("Oops!", "❗ Please enter a valid non-negative integer.")


root = tk.Tk()
root.title("√ Square Root Calculator")

tk.Label(root, text="Enter a non-negative integer:").pack(pady=5)
input_entry = tk.Entry(root, font=("Arial", 12))
input_entry.pack(pady=5)

compute_button = tk.Button(root, text="Calculate", command=compute_square_root)
compute_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="blue")
result_label.pack(pady=5)

root.mainloop()
