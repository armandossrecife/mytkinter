import tkinter as tk

root = tk.Tk()
my_label = tk.Label(root, text='starting...', font='Arial 36')
my_label.pack()

my_label.bind('<Enter>', lambda e: my_label.configure(text='mouse inside'))
my_label.bind('<Leave>', lambda e: my_label.configure(text='mouse outside'))
my_label.bind('<1>', lambda e: my_label.configure(text='mouse click'))

root.mainloop()