import tkinter as tk

janela = tk.Tk()
janela.title("Minha Aplicação")
janela.geometry("500x500")  # Defina o tamanho da janela

meu_rotulo = tk.Label(janela, text="Olá, Tkinter!")
meu_rotulo.pack()  # Empacote o rótulo na janela

janela.mainloop()