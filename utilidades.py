import tkinter

class HandleInputs:
    def __init__(self, lista_inputs:list) -> None:
        self.lista_inputs = lista_inputs

    def add_input(self, my_input:tkinter.Entry):
        self.lista_inputs.append(my_input)

    def limpar_input(self, campo:tkinter.Entry):
        campo.delete(0, tkinter.END)

    def limpar_inputs(self):
        for campo in self.lista_inputs:
            self.limpar_input(campo)


class Pack:
    def __init__(self, lista_elementos:list) -> None:
        self.lista_elementos = lista_elementos

    def update(self):
        for elemento in self.lista_elementos:
            elemento.pack()
