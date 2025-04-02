import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

# Inicializa o workbook e a worksheet
workbook = Workbook()
sheet = workbook.active
sheet.title = "Clientes"
sheet.append(["ID", "Nome", "Endereço", "Telefone", "Email"])  # Cabeçalhos da planilha

# Função para salvar os dados do cliente
def salvar_cliente():
    id_cliente = id_entry.get()
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()

    if id_cliente and nome and endereco and telefone and email:
        sheet.append([id_cliente, nome, endereco, telefone, email])
        id_entry.delete(0, tk.END)
        nome_entry.delete(0, tk.END)
        endereco_entry.delete(0, tk.END)
        telefone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")

# Função para finalizar e salvar o arquivo Excel
def salvar_arquivo():
    workbook.save("clientes.xlsx")
    messagebox.showinfo("Sucesso", "Arquivo 'clientes.xlsx' salvo com sucesso!")
    root.destroy()

# Cria a janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")

# Cria os campos e labels
tk.Label(root, text="ID do Cliente:").grid(row=0, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
nome_entry = tk.Entry(root)
nome_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço:").grid(row=2, column=0, padx=10, pady=5)
endereco_entry = tk.Entry(root)
endereco_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Telefone:").grid(row=3, column=0, padx=10, pady=5)
telefone_entry = tk.Entry(root)
telefone_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=4, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, padx=10, pady=5)

# Botões para salvar cliente e finalizar cadastro
tk.Button(root, text="Salvar Cliente", command=salvar_cliente).grid(row=5, column=0, padx=10, pady=20)
tk.Button(root, text="Finalizar e Salvar Arquivo", command=salvar_arquivo).grid(row=5, column=1, padx=10, pady=20)

# Loop principal da interface
root.mainloop()