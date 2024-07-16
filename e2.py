import tkinter as tk

def exibir_texto():
    texto_inserido = entrada.get()
    rotulo_resultado.config(text=f"Você digitou: {texto_inserido}")

# Crie a janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")

# Crie um rótulo
rotulo = tk.Label(root, text="Digite algo:")
rotulo.pack()

# Crie um campo de entrada de texto
entrada = tk.Entry(root)
entrada.pack()

# Crie um botão para exibir o texto
botao = tk.Button(root, text="Exibir", command=exibir_texto)
botao.pack()

# Rótulo para exibir o resultado
rotulo_resultado = tk.Label(root, text="")
rotulo_resultado.pack()

# Execute o loop principal da janela
root.mainloop()