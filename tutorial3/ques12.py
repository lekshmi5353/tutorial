import tkinter as tk

def convert_to_uppercase():
    text = input_entry.get()
    result_label.config(text=f"Uppercase: {text.upper()}")

root = tk.Tk()
root.title(" Uppercase Converter (Again)")

tk.Label(root, text="Type something:").pack(pady=5)
input_entry = tk.Entry(root, font=("Arial", 12))
input_entry.pack(pady=5)

convert_button = tk.Button(root, text="Make Uppercase!", command=convert_to_uppercase)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="green")
result_label.pack(pady=5)

root.mainloop()
