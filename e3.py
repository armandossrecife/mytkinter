import tkinter as tk

# Crie a janela principal
root = tk.Tk()
root.title("Exemplo com Grid")

# Crie alguns widgets com diferentes opções de grid
label1 = tk.Label(root, text="Label 1", bg="#ff9999")
label2 = tk.Label(root, text="Label 2", bg="#99ff99")
label3 = tk.Label(root, text="Label 3", bg="#9999ff")

# Posicione os widgets usando grid
label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=0, column=1, columnspan=2, ipadx=10, ipady=10)
label3.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

# Execute o loop principal da janela
root.mainloop()