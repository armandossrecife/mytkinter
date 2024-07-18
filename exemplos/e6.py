import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    texto_inserido = entrada.get()
    messagebox.showinfo("Mensagem", f"Você digitou: {texto_inserido}")

# Crie a janela principal
root = tk.Tk()
root.title("Tratamento de Entrada")

# Crie um campo de entrada de texto
entrada = tk.Entry(root)
entrada.pack()

# Crie um botão para exibir a mensagem
botao = tk.Button(root, text="Exibir", command=exibir_mensagem)
botao.pack()

# Execute o loop principal da janela
root.mainloop()