import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview - Multiple Columns")

# Create the Treeview widget
tree = ttk.Treeview(root)
tree.grid(padx=10, pady=10)  # Add padding for better appearance

# Define columns
tree['columns'] = ('size', 'modified')

# Configure columns
tree.column('size', width=50, anchor='center')
tree.heading('size', text='Size')
tree.column('modified', width=100, anchor='center')  # Adjust width as needed
tree.heading('modified', text='Modified')

# Insert items with values for multiple columns
tree.insert('', 'end', 'widgets', text='Widgets', values=('12KB', 'Last week'))
tree.insert('', 0, 'apps', text='Applications', values=('Unknown', 'N/A'))  # Set default values

tree.insert('', 'end', text='Canvas', values=('25KB', 'Today'))
tree.insert('apps', 'end', text='Browser', values=('115KB', 'Yesterday'))

root.mainloop()