import tkinter as tk
from tkinter import messagebox
import random


low, high = 1, 100
attempts = 0
computer_guess = random.randint(low, high)

def make_guess():
    global computer_guess, attempts
    guess_label.config(text=f"Is your number {computer_guess}?")
    attempts += 1

def check_response(response):
    global low, high, computer_guess
    if response == "Correct":
        messagebox.showinfo("🎉 Game Over", f"Computer guessed it in {attempts} tries!")
        root.quit()
    elif response == "Too small":
        low = computer_guess + 1
    elif response == "Too large":
        high = computer_guess - 1

   
    if low <= high:
        computer_guess = random.randint(low, high)
        make_guess()
    else:
        messagebox.showerror("Oops!", "🤔 No possible guesses left. Something went wrong!")


root = tk.Tk()
root.title("🤖 Computer Guessing Game")

guess_label = tk.Label(root, text="", font=("Arial", 14))
guess_label.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Too Small", command=lambda: check_response("Too small")).pack(side="left", padx=5)
tk.Button(button_frame, text="Too Large", command=lambda: check_response("Too large")).pack(side="left", padx=5)
tk.Button(button_frame, text="Correct", command=lambda: check_response("Correct")).pack(side="left", padx=5)

make_guess()

root.mainloop()
