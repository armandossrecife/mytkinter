import tkinter as tk
from tkinter import ttk  # Import ttk for themed widgets

root = tk.Tk()
root.title("Treeview")

# Create the Treeview widget
tree = ttk.Treeview(root)
tree.grid(padx=10, pady=10)  # Add padding for better appearance

# Insert items
tree.insert('', 0, text='Item 1')
tree.insert('', 'end', text='Item 2')

# Create a parent item and insert sub-items
parent_id = tree.insert('', 'end', text='Item 3')
tree.insert(parent_id, 0, text='sub-item 0')
tree.insert(parent_id, 1, text='sub-item 1')

root.mainloop()