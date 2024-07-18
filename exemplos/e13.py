
import tkinter as tk

class FontDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Font Showcase")

        # Create a frame to hold the labels
        self.frame = tk.Frame(self)
        self.frame.pack(padx=10, pady=10)

        # List of fonts
        fonts = ["Times", "Courier", "Helvetica", "Didot"]

        # Create and position labels with different fonts
        for i, font_name in enumerate(fonts):
            label = tk.Label(self.frame, text=font_name, font=(font_name, 24))
            label.grid(row=i, column=0, padx=5, pady=5)

if __name__ == "__main__":
    demo = FontDemo()
    demo.mainloop()