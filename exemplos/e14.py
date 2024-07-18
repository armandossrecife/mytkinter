import tkinter as tk
from PIL import Image, ImageTk

class ImageDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Label Demo")

        # Create a label for text
        self.text_label = tk.Label(self, text="Show icon", font="Arial 20")
        self.text_label.pack(padx=10, pady=10)

        # Load image
        try:
            icons_path = './icons'
            my_bell = icons_path + '/' + 'bell.png'
            self.image = Image.open(my_bell)
            self.photo_image = ImageTk.PhotoImage(self.image)
        except FileNotFoundError:
            print(f"Error: Image file {my_bell} not found.")
            return  # Exit if image is not found

        # Create label with image
        self.image_label = tk.Label(text='Bell', image=self.photo_image, compound='top')
        self.image_label.pack()

        # Create button with image
        self.image_button = tk.Button(text='Bell', image=self.photo_image, compound='top')
        self.image_button.pack()

if __name__ == "__main__":
    demo = ImageDemo()
    demo.mainloop()