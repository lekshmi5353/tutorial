import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{celsius:.1f}")
    except ValueError:
        messagebox.showerror("Oops!", "❗ Please enter a valid Fahrenheit value.")

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit:.1f}")
    except ValueError:
        messagebox.showerror("Oops!", "❗ Please enter a valid Celsius value.")


root = tk.Tk()
root.title("🌡️ Temperature Converter")


tk.Label(root, text="Fahrenheit:").grid(row=0, column=0, padx=10, pady=5)
fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=1, column=0)
fahrenheit_entry.insert(0, "32")  # Default value

tk.Label(root, text="Celsius:").grid(row=0, column=1, padx=10, pady=5)
celsius_entry = tk.Entry(root)
celsius_entry.grid(row=1, column=1)
celsius_entry.insert(0, "0.0")  # Default value


tk.Button(root, text=">>>> Convert to Celsius", command=fahrenheit_to_celsius).grid(row=2, column=0, pady=10)
tk.Button(root, text="<<<< Convert to Fahrenheit", command=celsius_to_fahrenheit).grid(row=2, column=1, pady=10)

root.mainloop()
