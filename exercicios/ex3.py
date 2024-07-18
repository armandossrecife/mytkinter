import tkinter as tk
import janelas

def mostrar_imagem():
  show_image = janelas.WindowImageViewer(image_path=campo_caminho_imagem.get(), main_window=janela_principal) 
  show_image.app.mainloop()

# Criar a janela principal
janela_principal = tk.Tk()
janela_principal.title("Visualizador de Imagens")

# Rótulo para o título do formulário
rotulo_titulo = tk.Label(janela_principal, text="Caminho da Imagem")
rotulo_titulo.pack()

# Entrada para o caminho da imagem
campo_caminho_imagem = tk.Entry(janela_principal)
campo_caminho_imagem.pack()

# Botão para mostrar a imagem
botao_mostrar_imagem = tk.Button(janela_principal, text="Mostrar Imagem", command=mostrar_imagem)
botao_mostrar_imagem.pack()

# Executar o loop principal da interface
janela_principal.mainloop()