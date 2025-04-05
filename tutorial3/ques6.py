import tkinter as tk

def convert_to_uppercase():
    result_label.config(text=input_entry.get().upper())


root = tk.Tk()
root.title("Uppercase Converter")

tk.Label(root, text="Enter some text:").pack(pady=5)
input_entry = tk.Entry(root, font=("Arial", 12))
input_entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="green")
result_label.pack(pady=5)

root.mainloop()
