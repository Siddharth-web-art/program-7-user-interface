import tkinter as tk
from tkinter import messagebox

def sort_words():
    input_text = entry.get()
    words = input_text.split('-')
    words.sort()
    sorted_text = '-'.join(words)
    messagebox.showinfo("Sorted Words", sorted_text)

# Create the main window
root = tk.Tk()
root.title("Word Sorter")

# Create and place the input label and entry
label = tk.Label(root, text="Enter hyphen-separated words:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create and place the sort button
sort_button = tk.Button(root, text="Sort Words", command=sort_words)
sort_button.pack(pady=10)

# Run the application
root.mainloop()