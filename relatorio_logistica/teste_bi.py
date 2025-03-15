import pandas as pd
import random

# Gerando dados fictícios para o relatório logístico
dados = {
    "ID": [i for i in range(1, 101)],
    "Data": pd.date_range(start="2025-01-01", periods=100).strftime('%d/%m/%Y').tolist(),
    "Origem": [random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Recife"]) for _ in range(100)],
    "Destino": [random.choice(["Curitiba", "Salvador", "Fortaleza", "Brasília"]) for _ in range(100)],
    "Produto": [random.choice(["Eletrônicos", "Vestuário", "Alimentos", "Medicamentos"]) for _ in range(100)],
    "Quantidade": [random.randint(10, 500) for _ in range(100)],
    "Peso (Kg)": [round(random.uniform(5, 50), 2) for _ in range(100)],
    "Custo (R$)": [round(random.uniform(100, 5000), 2) for _ in range(100)],
    "Status": [random.choice(["Em trânsito", "Entregue", "Aguardando retirada"]) for _ in range(100)],
    "Transportadora": [random.choice(["Transportadora X", "Transportadora Y", "Transportadora Z"]) for _ in range(100)],
}

# Criando o DataFrame
relatorio = pd.DataFrame(dados)

# Criando a coluna Categoria baseada na Quantidade
def categorizar_quantidade(quantidade):
    if quantidade >= 300:
        return "Alta"
    elif quantidade >= 100:
        return "Média"
    else:
        return "Baixa"

relatorio["Categoria"] = relatorio["Quantidade"].apply(categorizar_quantidade)

# Exportando para CSV
relatorio.to_csv("relatorio_logistica_categorias.csv", index=False, encoding="utf-8-sig", sep=";")

print("Relatório logístico com categorias gerado e exportado para 'relatorio_logistica_categorias.csv'!")
