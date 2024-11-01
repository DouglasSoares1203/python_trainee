

import openpyxl
from openpyxl import Workbook

# Criar um novo arquivo Excel
wb = Workbook()

# Selecionar a planilha ativa
sheet = wb.active

# Definir título da planilha
sheet.title = "Dados"

# Criar função para adicionar dados
def adicionar_dados():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite sua cidade: ")

    # Adicionar dados na planilha
    sheet.append([nome, idade, cidade])

    # Salvar arquivo Excel
    wb.save("dados.xlsx")

# Chamar função
adicionar_dados()


# Nesse código:

# - Importamos a biblioteca openpyxl.
# - Criamos um novo arquivo Excel com Workbook().
# - Selecionamos a planilha ativa com wb.active.
# - Definimos título da planilha com sheet.title.
# - Criamos uma função adicionar_dados() para coletar dados do usuário.
# - Adicionamos dados na planilha com sheet.append().
# - Salvamos o arquivo Excel com wb.save().

# Execute o código e veja os dados sendo adicionados ao arquivo Excel!

# Dica: você pode personalizar o código para:

# - Adicionar mais colunas ou linhas.
# - Validar dados de entrada.
# - Usar formulários para coletar dados.
# - Integrar com bancos de dados.

# Bibliotecas úteis:

# - openpyxl: para trabalhar com arquivos Excel.
# - pandas: para manipular dados em DataFrame.
# - tkinter: para criar interfaces gráficas.
