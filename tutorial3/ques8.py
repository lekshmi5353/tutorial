import tkinter as tk
from tkinter import messagebox
import random


target_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1

        if guess < target_number:
            feedback_label.config(text="Too small! Try again.")
        elif guess > target_number:
            feedback_label.config(text=" Too large! Try again.")
        else:
            feedback_label.config(text=f"🎉 You got it! Attempts: {attempts}")
            messagebox.showinfo("Congratulations!", f"You guessed it in {attempts} tries!")
            root.quit()
    except ValueError:
        messagebox.showerror("Oops!", "❗ Please enter a valid number.")


root = tk.Tk()
root.title("🎯 Guess the Number Game")

tk.Label(root, text="I'm thinking of a number between 1 and 100!", font=("Arial", 14)).pack(pady=10)
guess_entry = tk.Entry(root, font=("Arial", 12))
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess!", command=check_guess)
guess_button.pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="red")
feedback_label.pack(pady=5)

root.mainloop()
