import tkinter as tk
from tkinter import messagebox

def calculate_distance():
    try:
        initial_height = float(height_entry.get())
        bounciness_index = float(bounciness_entry.get())
        bounces = int(bounces_entry.get())
        
        if initial_height <= 0 or bounciness_index <= 0 or bounces < 0:
            raise ValueError("Invalid input values.")
        
        total_distance = initial_height
        height_after_bounce = initial_height

        for _ in range(bounces):
            height_after_bounce *= bounciness_index
            total_distance += 2 * height_after_bounce  # Going down and up

        result_label.config(text=f"Total Distance Traveled: {total_distance:.2f} meters")
    except ValueError:
        messagebox.showerror("Oops!", "❗ Please enter valid positive numbers.")


root = tk.Tk()
root.title(" Bouncy Ball Distance Calculator")


tk.Label(root, text="Initial Height (m):").grid(row=0, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=0)
height_entry.insert(0, "10")

tk.Label(root, text="Bounciness Index:").grid(row=0, column=1, padx=10, pady=5)
bounciness_entry = tk.Entry(root)
bounciness_entry.grid(row=1, column=1)
bounciness_entry.insert(0, "0.9")

tk.Label(root, text="Number of Bounces:").grid(row=0, column=2, padx=10, pady=5)
bounces_entry = tk.Entry(root)
bounces_entry.grid(row=1, column=2)
bounces_entry.insert(0, "5")


calculate_button = tk.Button(root, text="Calculate Distance", command=calculate_distance)
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)



result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="blue")
result_label.grid(row=3, column=0, columnspan=3, pady=5)

root.mainloop()
