import pandas as pd
import requests

# URL base da API (exemplo fictício, substitua pelo URL correto)
api_url = "https://telaflixapi.com/e/movie"

# Lista de filmes para consulta
filmes = [
    {"Filme": "Inception", "Ano": 2010},
    {"Filme": "The Matrix", "Ano": 1999},
    {"Filme": "Interstellar", "Ano": 2014},
    {"Filme": "Tesouro", "Ano": 2024},
    {"Filme": "Ameaça no Ar", "Ano": 2025},

]

# Função para chamar a API e retornar os dados
def buscar_dados(filme):
    try:
        # Construindo os parâmetros da consulta
        params = {"title": filme["Filme"], "year": filme["Ano"]}
        response = requests.get(api_url, params=params)
        
        # Verificando o status da resposta
        if response.status_code == 200:
            return response.json()  # Retorna os dados no formato JSON
        else:
            return {"Erro": f"Status {response.status_code}"}  # Caso haja erro na resposta
    except Exception as e:
        return {"Erro": str(e)}  # Captura e retorna exceções

# Criar um DataFrame com as colunas "Filme" e "Ano"
df = pd.DataFrame(filmes)

# Adicionar coluna com os dados retornados pela API
df["Dados_API"] = df.apply(buscar_dados, axis=1)

# Mostrar o DataFrame resultante
print(df)