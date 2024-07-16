import tkinter
from tkinter import messagebox

class MyWindow():
    def __init__(self, title=None):
        self.root = tkinter.Tk()
        if title:
            self.root.title(title)

    def add_components(self):
        self.my_label_nome = tkinter.Label(self.root, text="Nome")
        self.my_text_nome = tkinter.Entry(self.root)
        self.my_button_info = tkinter.Button(self.root, text="Info", command=self.show_message)
        # A passagem de parametros em uma chamada metodo do command de button precisa usar a funcao lambda
        self.my_button_nome = tkinter.Button(self.root, text="Ok", command=lambda: self.show_message_conteudo(self.my_text_nome.get()))
        self.my_label_nome.pack()
        self.my_text_nome.pack()
        self.my_button_info.pack()
        self.my_button_nome.pack()

    def show_message(self):
        messagebox.showinfo(title="Info", message="Bem vindo ao Tkinter!")

    def show_message_conteudo(self, conteudo):
        messagebox.showinfo(title="Info", message=conteudo)

    def exec(self):
        self.root.mainloop()

my_app = MyWindow()
my_app.add_components()
my_app.exec()