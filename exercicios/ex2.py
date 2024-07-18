import tkinter
import os
from tkinter import messagebox

def show_content():
    path_file = entry_path_arquivo.get()
    if path_file:
        filename = os.path.basename(path_file)
        with open(path_file, mode='r') as file:
            conteudo = file.read()
            text_conteudo.delete(1.0, tkinter.END)
            text_conteudo.insert(tkinter.END, conteudo)
    else:
        messagebox.showwarning(title='Dados incompletos', message='Informe o caminho do arquivo')

aplicacao = tkinter.Tk()
aplicacao.title('Mostra o conteúdo de um arquivo')

# Adicionar os componentes
label_path_arquivo = tkinter.Label(aplicacao, text="Caminho do arquivo")
entry_path_arquivo = tkinter.Entry(aplicacao)
text_conteudo = tkinter.Text(aplicacao, width=40, height=10)
button_mostra = tkinter.Button(aplicacao, text="Mostra conteúdo", command=show_content)

# Empacota os componentes
label_path_arquivo.pack()
entry_path_arquivo.pack()
text_conteudo.pack()
text_conteudo.pack()
button_mostra.pack()

# Executa a aplicacao
aplicacao.mainloop()