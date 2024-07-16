import tkinter
from tkinter import messagebox

class MyWindow():
    def __init__(self, title=None):
        self.root = tkinter.Tk()
        if title:
            self.root.title(title)

    def add_components(self):
        self.my_label_nome = tkinter.Label(self.root, text="Nome")
        self.my_button_info = tkinter.Button(self.root, text="Info", command=self.show_message)
        self.my_label_nome.pack()
        self.my_button_info.pack()

    def show_message(self):
        messagebox.showinfo(title="Info", message="Bem vindo ao Tkinter!")

    def exec(self):
        self.root.mainloop()

my_app = MyWindow()
my_app.add_components()
my_app.exec()