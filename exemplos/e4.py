import tkinter as tk

# Crie a janela principal
root = tk.Tk()
root.title("Exemplo com Place")

# Crie alguns widgets com posições específicas
label1 = tk.Label(root, text="Widget 1", bg="#ff9999")
label2 = tk.Label(root, text="Widget 2", bg="#99ff99")
label3 = tk.Label(root, text="Widget 3", bg="#9999ff")

# Posicione os widgets usando o gerenciador place
label1.place(x=50, y=20)
label2.place(x=100, y=80)
label3.place(x=200, y=150)

# Execute o loop principal da janela
root.mainloop()