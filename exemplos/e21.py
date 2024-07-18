import tkinter as tk
from tkinter import filedialog, colorchooser

class Demo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Windows and dialogs')

        # Label
        label = tk.Label(self, text='Standard Dialogs', font='Arial 24')
        label.pack(padx=10, pady=10)

        # Buttons with functions
        self.open_button = tk.Button(self, text='Open...', command=self.open_file)
        self.open_button.pack(padx=10, pady=5)

        self.save_button = tk.Button(self, text='Save...', command=self.save_file)
        self.save_button.pack(padx=10, pady=5)

        self.dir_button = tk.Button(self, text='Directory...', command=self.open_dir)
        self.dir_button.pack(padx=10, pady=5)

        self.color_button = tk.Button(self, text='Select color...', command=self.select_color)
        self.color_button.pack(padx=10, pady=5)

        # Labels for displaying selected values
        self.open_label = tk.Label(self, text='File')
        self.open_label.pack(padx=10, pady=5)

        self.save_label = tk.Label(self, text='File')
        self.save_label.pack(padx=10, pady=5)

        self.dir_label = tk.Label(self, text='Directory')
        self.dir_label.pack(padx=10, pady=5)

        self.color_label = tk.Label(self, text='Color')
        self.color_label.pack(padx=10, pady=5)

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.open_label.config(text=filename)

    def save_file(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            self.save_label.config(text=filename)

    def open_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_label.config(text=directory)

    def select_color(self):
        color_tuple = colorchooser.askcolor()
        if color_tuple:  # Check if user canceled
            color_hex = colorchooser.RGBtoHex(color_tuple[0])  # Convert to hex for display
            self.color_label.config(text=color_hex)


if __name__ == '__main__':
    demo = Demo()
    demo.mainloop()