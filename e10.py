import tkinter
import utilidades
from tkinter import messagebox

def show_message():
  messagebox.showinfo(title="My Message", message="This is an informative message.")

def concatena_nome_sobrenome():
    nome = input_nome.get()
    sobrenome = input_sobrenome.get()
    resultado = nome + " " + sobrenome
    messagebox.showinfo(title="My Message", message=resultado)
    app.destroy()
    
# Cria a app que ser a janela principal
app = tkinter.Tk()
app.title("Minha App Gui (GRID)")

# Cria os paineis para acomodar os widgets
my_panel_inputs = tkinter.Frame(app)
my_panel_buttons = tkinter.Frame(app)

# Cria os widgets de lables e inputs
label_nome = tkinter.Label(my_panel_inputs, text="Nome")
label_sobrenome = tkinter.Label(my_panel_inputs, text="Sobrenome")
input_nome = tkinter.Entry(my_panel_inputs)
input_sobrenome = tkinter.Entry(my_panel_inputs)
lista_inputs = [input_nome, input_sobrenome]

# Cria um manipulador de inputs
manipula_campos = utilidades.HandleInputs(lista_inputs)

# Cria os widgets de botao
button_limpar = tkinter.Button(my_panel_buttons, text="Limpar", command=manipula_campos.limpar_inputs)
button_sair = tkinter.Button(my_panel_buttons, text="Sair", command=concatena_nome_sobrenome)

# Define o Grid do 1o painel (my_panel_inputs)
label_nome.grid(row=0, column=0)
label_sobrenome.grid(row=1, column=0)
input_nome.grid(row=0, column=1)
input_sobrenome.grid(row=1, column=1)

# Define o Grid do 2o. painel (my_panel_buttons)
button_limpar.grid(row=0, column=0)
button_sair.grid(row=0, column=1)

# Adiciona os panels na janela principal (app)
my_panel_inputs.pack()
my_panel_buttons.pack()

app.mainloop()
