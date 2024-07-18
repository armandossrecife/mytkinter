import tkinter as tk
from tkinter import ttk  # Import ttk for themed widgets (scrollbar)

root = tk.Tk()
root.title("Listbox with Scrollbar")

# Create a label
label = tk.Label(root, text="Listbox with scrollbars", font="Arial 18")
label.pack(padx=10, pady=10)

# Create a list of strings for the listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "This is a longer item", ...]  # Add more items as needed

# Create a listbox with scrollbar
lb = tk.Listbox(root, listvariable=tk.StringVar(value=items))  # Use tk.StringVar for listbox data
sb = ttk.Scrollbar(root, orient='vertical')  # Specify vertical scrollbar

# Layout and configuration
sb.pack(side=tk.RIGHT, fill=tk.Y)  # Scrollbar on the right, fill vertically
lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Listbox on the left, fill both sides, expand

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

root.mainloop()