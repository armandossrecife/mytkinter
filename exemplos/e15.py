import tkinter as tk

class TkinterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Button and Motion Events")

        # Labels
        self.title_label = tk.Label(self, text="Button and Motion Events", font="Arial 24")
        self.title_label.pack(padx=10, pady=10)
        self.status_label = tk.Label(self, text="Display the event in the status bar")
        self.status_label.pack()

        # Status bar initialization (optional)
        # Assuming you want a separate status bar widget
        self.status_bar = tk.Label(self, text="", bd=1, relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Event bindings
        self.bind('<Button>', self.on_click)
        self.bind('<Motion>', self.on_motion)

    def on_click(self, event):
        """Callback for button click event."""
        x, y = event.x, event.y
        self.status_bar.config(text=f"Button clicked at ({x}, {y})")

    def on_motion(self, event):
        """Callback for mouse movement event."""
        x, y = event.x, event.y
        self.status_bar.config(text=f"Mouse moved to ({x}, {y})")

if __name__ == "__main__":
    app = TkinterApp()
    app.mainloop()