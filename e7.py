import tkinter as tk

# Cria a instância principal da Tkinter
root = tk.Tk()

# Cria a barra de menus principal
menubar = tk.Menu(root)

# Cria um menu suspenso para "Arquivo"
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Novo", command=lambda: print("Novo Arquivo"))
filemenu.add_command(label="Abrir", command=lambda: print("Abrir Arquivo"))
filemenu.add_separator()
filemenu.add_command(label="Sair", command=root.quit)

# Adiciona o menu "Arquivo" à barra de menus principal
menubar.add_cascade(label="Arquivo", menu=filemenu)

# Cria um menu suspenso para "Editar"
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Desfazer", command=lambda: print("Desfazer"))
editmenu.add_command(label="Refazer", command=lambda: print("Refazer"))
editmenu.add_separator()
editmenu.add_command(label="Copiar", command=lambda: print("Copiar"))
editmenu.add_command(label="Colar", command=lambda: print("Colar"))

# Adiciona o menu "Editar" à barra de menus principal
menubar.add_cascade(label="Editar", menu=editmenu)

# Configura a barra de menus principal como menu da janela
root.config(menu=menubar)

# Cria um rótulo para exibir o conteúdo da interface
label = tk.Label(root, text="Interface Principal")
label.pack()

# Exibe a janela principal
root.mainloop()
