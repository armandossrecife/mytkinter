import tkinter as tk

# Cria a instância principal da Tkinter
root = tk.Tk()

# Cria variáveis ​​vinculadas a widgets
nome_var = tk.StringVar()
idade_var = tk.IntVar()

# Cria um rótulo para o nome
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()

# Cria um campo de entrada para o nome e vincula à variável nome_var
nome_entry = tk.Entry(root, textvariable=nome_var)
nome_entry.pack()

# Cria um rótulo para a idade
idade_label = tk.Label(root, text="Idade:")
idade_label.pack()

# Cria um campo de entrada para a idade e vincula à variável idade_var
idade_entry = tk.Entry(root, textvariable=idade_var)
idade_entry.pack()

# Cria um botão para exibir os dados
def exibir_dados():
  nome = nome_var.get()
  idade = idade_var.get()
  print(f"Nome: {nome}, Idade: {idade}")

button = tk.Button(root, text="Exibir Dados", command=exibir_dados)
button.pack()

# Exibe a janela principal
root.mainloop()
