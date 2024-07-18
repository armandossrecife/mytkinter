import tkinter as tk

# Create the main window
root = tk.Tk()  # Use tk.Tk() for the main window
root.title("Canvas with Ovals and Text")

# Create the canvas widget
c = tk.Canvas(root, width=600, height=300, background='lightblue')
c.pack()  # Add the canvas to the main window

# Create lines
c.create_line(10, 10, 200, 200, fill='red')
c.create_line(20, 10, 210, 200, fill='blue', width=3)

# Create ovals
c.create_oval(100, 200, 150, 250, fill='green', width=2)
c.create_oval(300, 100, 580, 250, fill='yellow', width=5)

# Create text labels
c.create_text(300, 150, text="Python", font='Arial 48')
c.create_text(300, 250, text="Canvas", font='Zapfino 72')

# Start the main loop
root.mainloop()