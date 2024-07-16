import tkinter as tk

# Cria a instância principal da Tkinter
root = tk.Tk()

# Cria um rótulo para exibir texto
label = tk.Label(root, text="Rótulo Inicial")
label.pack()

# Função para mudar a cor do rótulo para vermelho
def mudar_cor_para_vermelho():
  label.config(fg="red")

# Função para mudar a cor do rótulo para azul
def mudar_cor_para_azul():
  label.config(fg="blue")

# Cria botões para mudar a cor do rótulo
button_vermelho = tk.Button(root, text="Vermelho", command=mudar_cor_para_vermelho)
button_vermelho.pack()

button_azul = tk.Button(root, text="Azul", command=mudar_cor_para_azul)
button_azul.pack()

# Exibe a janela principal
root.mainloop()
