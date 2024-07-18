import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class TableView(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)

        self.data = data  # Store data for sorting

        # Create the Treeview
        columns = [str(i) for i in range(len(data[0]))]
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Define headings based on the data provided
        for i, col in enumerate(columns):
            self.tree.heading(col, text=f"Column {i+1}")

        # Insert data into the Treeview
        for row in self.data:
            self.tree.insert('', 'end', values=row)

        # Configure columns after data insertion
        self.configure_columns()

    def configure_columns(self):
        """
        Configure the columns to fit the content and set a minimum width.
        """
        font = tkFont.Font()
        for col in self.tree['columns']:
            self.tree.column(col, minwidth=100)
            max_width = font.measure(self.tree.heading(col, 'text'))  # Measure column header width
            for item in self.tree.get_children():
                text = self.tree.item(item, 'values')[int(col)]
                col_width = font.measure(text)
                max_width = max(max_width, col_width)
            self.tree.column(col, width=max_width)

# Sample data for testing
data = [
    ['Item 1', 'Value 1.1', 'Value 1.2'],
    ['Item 2', 'Value 2.1', 'Value 2.2 (longer value)'],
    ['Item 3', 'Value 3.1', 'Value 3.2']
]

# Main application window
root = tk.Tk()
root.title("Table View Example")

# Create TableView instance
table_view = TableView(root, data)
table_view.pack(fill=tk.BOTH, expand=True)

root.mainloop()