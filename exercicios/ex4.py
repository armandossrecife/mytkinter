import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os contatos (nome: telefone)
contatos = {}

root = tk.Tk()
root.title("Agenda Telefônica")

# Função para adicionar um novo contato
def adicionar_contato():
    nome = campo_nome_novo.get().strip()
    telefone = campo_telefone_novo.get().strip()

    if nome == "" or telefone == "":
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    if nome in contatos:
        messagebox.showwarning("Aviso", f"O contato '{nome}' já existe!")
        return

    contatos[nome] = telefone
    # Limpa os campos de entrada (nome e telefone)
    campo_nome_novo.delete(0, tk.END)
    campo_telefone_novo.delete(0, tk.END)
    # Limpa os campos de pesquisa
    campo_nome_pesquisa.delete(0, tk.END)
    campo_nome_editar.delete(0, tk.END)
    campo_telefone_editar.delete(0, tk.END)

    # Atualiza o listbox de contatos
    atualizar_lista_contatos()
    messagebox.showinfo("Sucesso", "Contato adicionado!")
    campo_nome_novo.focus_set()

# Função para editar um contato
def editar_contato():
    nome_pesquisado = campo_nome_pesquisa.get().strip()
    novo_nome = campo_nome_editar.get().strip()
    novo_telefone = campo_telefone_editar.get().strip()

    if nome_pesquisado == "" or novo_nome == "" or novo_telefone == "":
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    if nome_pesquisado not in contatos:
        messagebox.showwarning("Aviso", f"O contato '{nome_pesquisado}' não existe!")
        return

    del contatos[nome_pesquisado]
    contatos[novo_nome] = novo_telefone
    # Limpa os campos de entrada (nome e telefone)
    campo_nome_pesquisa.delete(0, tk.END)
    campo_nome_editar.delete(0, tk.END)
    campo_telefone_editar.delete(0, tk.END)
    # Atualiza o listbox de contatos
    atualizar_lista_contatos()
    messagebox.showinfo("Sucesso", "Contato editado!")

# Função para excluir um contato
def excluir_contato():
    nome_pesquisado = campo_nome_pesquisa.get().strip()

    if nome_pesquisado == "":
        messagebox.showerror("Erro", "Preencha o campo de pesquisa!")
        return

    if nome_pesquisado not in contatos:
        messagebox.showwarning("Aviso", f"O contato '{nome_pesquisado}' não existe!")
        return

    if messagebox.askokcancel("Confirmação", f"Deseja realmente excluir o contato '{nome_pesquisado}'?"):
        del contatos[nome_pesquisado]
        campo_nome_pesquisa.delete(0, tk.END)
        atualizar_lista_contatos()
        messagebox.showinfo("Sucesso", "Contato excluído!")
        campo_nome_pesquisa.delete(0, tk.END)
        campo_nome_editar.delete(0, tk.END)
        campo_telefone_editar.delete(0, tk.END)

# Função para atualizar a lista de contatos
def atualizar_lista_contatos():
    # Limpa o listbox
    listbox_contatos.delete(0, tk.END)
    # Atualiza o listbox de contatos
    for nome, telefone in contatos.items():
        listbox_contatos.insert(tk.END, f"{nome}: {telefone}")

# Função para selecionar contato na lista
# Captura o evento de clique no item selecoionado do listbox
def selecionar_contato(event):
    try:
        indice_selecionado = listbox_contatos.curselection()[0]
        contato_selecionado = listbox_contatos.get(indice_selecionado)
        nome, telefone = contato_selecionado.split(": ")
        campo_nome_pesquisa.delete(0, tk.END)
        campo_nome_pesquisa.insert(0, nome)
        campo_nome_editar.delete(0, tk.END)
        campo_nome_editar.insert(0, nome)
        campo_telefone_editar.delete(0, tk.END)
        campo_telefone_editar.insert(0, telefone)
    except IndexError:
        messagebox.showerror("Erro ao selecionar contato!")

# Função para listar todos os contatos
def listar_contatos():
    atualizar_lista_contatos()

# Seção (Frame) para adicionar novo contato
frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)
# Adiciona os widgets no Frame
tk.Label(frame_adicionar, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
campo_nome_novo = tk.Entry(frame_adicionar)
campo_nome_novo.grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame_adicionar, text="Telefone:").grid(row=1, column=0, padx=5, pady=5)
campo_telefone_novo = tk.Entry(frame_adicionar)
campo_telefone_novo.grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_adicionar, text="Adicionar", command=adicionar_contato).grid(row=2, columnspan=2, pady=10)

# Seção (Frame) para editar e excluir contatos
frame_editar_excluir = tk.Frame(root)
frame_editar_excluir.pack(pady=10)
# Adiciona os widgets no Frame
tk.Label(frame_editar_excluir, text="Pesquisar por Nome:").grid(row=0, column=0, padx=5, pady=5)
campo_nome_pesquisa = tk.Entry(frame_editar_excluir)
campo_nome_pesquisa.grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame_editar_excluir, text="Novo Nome:").grid(row=1, column=0, padx=5, pady=5)
campo_nome_editar = tk.Entry(frame_editar_excluir)
campo_nome_editar.grid(row=1, column=1, padx=5, pady=5)
tk.Label(frame_editar_excluir, text="Novo Telefone:").grid(row=2, column=0, padx=5, pady=5)
campo_telefone_editar = tk.Entry(frame_editar_excluir)
campo_telefone_editar.grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame_editar_excluir, text="Editar", command=editar_contato).grid(row=3, column=0, pady=10)
tk.Button(frame_editar_excluir, text="Excluir", command=excluir_contato).grid(row=3, column=1, pady=10)

# Frame com Lista de contatos com barra de rolagem
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10, fill=tk.BOTH, expand=True)
# Adiciona os widgets no Frame
listbox_contatos = tk.Listbox(frame_lista, selectmode=tk.SINGLE)
listbox_contatos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=listbox_contatos.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_contatos.config(yscrollcommand=scrollbar.set)
listbox_contatos.bind("<<ListboxSelect>>", selecionar_contato)

# Atualizar a lista de contatos inicialmente
atualizar_lista_contatos()

# Iniciar a interface gráfica
root.mainloop()