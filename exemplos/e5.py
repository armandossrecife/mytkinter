import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    messagebox.showinfo("Mensagem", "Você clicou no botão!")

# Crie a janela principal
root = tk.Tk()
root.title("Exemplo de Eventos")

# Crie um botão
botao = tk.Button(root, text="Clique aqui", command=exibir_mensagem)
botao.pack()

# Execute o loop principal da janela
root.mainloop()