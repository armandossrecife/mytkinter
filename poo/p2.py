import tkinter

class MyWindow():
    def __init__(self) -> None:
        self.root = tkinter.Tk()

    def add_components(self):
        self.my_label = tkinter.Label(self.root, text="Label1")
        self.my_button = tkinter.Button(self.root, text="Button1")
        self.my_label.pack()
        self.my_button.pack()

    def exec(self):
        self.root.mainloop()

my_app = MyWindow()
my_app.add_components()
my_app.exec()