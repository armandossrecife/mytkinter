import tkinter
import PIL.Image
import PIL.ImageTk
import os

class AplicacaoGUI():
    def __init__(self, titulo):
        self.root = tkinter.Tk()
        self.root.title(titulo)

    def executa(self):
        self.root.mainloop()

class WindowImageViewer:
  def __init__(self, image_path, main_window):
    self.app = tkinter.Toplevel()
    self.app.title("View Image")
    
    # Store reference to parent window
    self.main_window = main_window

    # Create a frame to hold the image
    self.image_frame = tkinter.Frame(self.app)
    
    # Error handling: Check if image exists before loading
    if not os.path.exists(image_path):
        self.show_error_message("Imagem não existe!")
        return

    # Load image using PIL
    self.image = PIL.Image.open(image_path)
    self.image_frame.pack(expand=True, fill=tkinter.BOTH)

    self.create_widgets(image_path)  # Separate function to create widgets

    # Bind the close button to the destroy function
    self.app.protocol("WM_DELETE_WINDOW", self.destroy)

  def create_widgets(self, image_path):
    """
    Creates the canvas, scrollbars, and displays the image.

    Args:
      image_path: The path to the image file to be displayed.
    """
    self.canvas = tkinter.Canvas(self.image_frame, relief=tkinter.SUNKEN)
    self.canvas.config(width=800, height=600, highlightthickness=0)

    self.sbarV = tkinter.Scrollbar(self.image_frame, orient=tkinter.VERTICAL)
    self.sbarH = tkinter.Scrollbar(self.image_frame, orient=tkinter.HORIZONTAL)

    self.sbarV.config(command=self.canvas.yview)
    self.sbarH.config(command=self.canvas.xview)

    self.canvas.config(yscrollcommand=self.sbarV.set)
    self.canvas.config(xscrollcommand=self.sbarH.set)

    self.sbarV.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    self.sbarH.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    self.canvas.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

    self.display_image(image_path)  # Separate function to display the image

  def display_image(self, image_path):
    """
    Opens the image, sets scroll region, and displays it.

    Args:
      image_path: The path to the image file to be displayed.
    """
    try:
      self.image = PIL.Image.open(image_path)
      width, height = self.image.size
      self.canvas.config(scrollregion=(0, 0, width, height))
      self.image2 = PIL.ImageTk.PhotoImage(self.image)
      self.imgtag = self.canvas.create_image(0, 0, anchor="nw", image=self.image2)
    except FileNotFoundError:
      print("Error: Image file not found!")

  def show_error_message(self, message):
    self.app = tkinter.Toplevel()
    self.app.title("Error")
    tkinter.Label(self.app, text=message).pack()

  def destroy(self):
    self.app.destroy()