import tkinter
from tkinter import messagebox

def show_message():
    mensagem = f"Seu nome é: {entry_nome.get()}, data de nascimento: {entry_data_nascimento.get()}"
    messagebox.showinfo(title="Mensagem", message=mensagem)

# Captura o evento (event) da tecla Enter
def show_message_on_press_enter(event):
    mensagem = f"Seu nome é: {entry_nome.get()}, data de nascimento: {entry_data_nascimento.get()}"
    messagebox.showinfo(title="Mensagem", message=mensagem)

aplicacao = tkinter.Tk()
aplicacao.title('Nome e idade')

# Adicione os componentes da aplicacao
label_nome = tkinter.Label(aplicacao, text="Nome")
entry_nome = tkinter.Entry(aplicacao)
label_data_nascimento = tkinter.Label(aplicacao, text="Data de nascimento")
entry_data_nascimento = tkinter.Entry(aplicacao)
button_show = tkinter.Button(aplicacao, text="Mostra dados", command=show_message)

# Empacota os componentes na aplicacao
label_nome.pack()
entry_nome.pack()
label_data_nascimento.pack()
entry_data_nascimento.pack()
button_show.pack()

# Vincula o evento de captura da tecla Enter
aplicacao.bind('<Return>', show_message_on_press_enter)

# Executa a aplicacao
aplicacao.mainloop()