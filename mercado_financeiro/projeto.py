import os
import time
import yfinance as yf
import pandas as pd

# Cria a pasta 'mercado_financeiro' se não existir
output_folder = "mercado_financeiro"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Função para obter dados do mercado financeiro
def obter_dados_financeiros(tickers):
    dados = []
    for ticker in tickers:
        acao = yf.Ticker(ticker)
        historico = acao.history(period="1d")  # Dados do último dia
        ultima_linha = historico.iloc[-1]  # Seleciona os dados mais recentes
        # Adiciona os dados em formato de dicionário
        dados.append({
            "Ticker": ticker,
            "Data": ultima_linha.name.date(),
            "Abertura": ultima_linha["Open"],
            "Alta": ultima_linha["High"],
            "Baixa": ultima_linha["Low"],
            "Fechamento": ultima_linha["Close"],
            "Volume": ultima_linha["Volume"],
            "Variação Diária": ultima_linha["High"] - ultima_linha["Low"],
            "Variação Percentual": ((ultima_linha["Close"] - ultima_linha["Open"]) / ultima_linha["Open"]) * 100,
            "Última Atualização": time.strftime("%Y-%m-%d %H:%M:%S")
        })
    return dados

# Lista de símbolos de ações que você deseja monitorar
tickers = tickers = ["AAPL", "MSFT", "GOOGL", "BBAS3.SA", "BBDC4.SA", "PETR4.SA"]  # Incluindo Banco do Brasil, Bradesco e Petrobras

# Loop para atualizar os dados periodicamente
# Loop para atualizar os dados periodicamente
while True:
    try:
        # Obtém os dados mais recentes
        dados = obter_dados_financeiros(tickers)

        # Cria um DataFrame com os dados obtidos
        df = pd.DataFrame(dados)

        # Caminho do arquivo Excel
        output_path = os.path.join(output_folder, "dados_mercado.xlsx")

        # Salva no arquivo Excel
        df.to_excel(output_path, index=False)
        print(f"Dados atualizados e salvos em: {output_path}")

        # Interrompe o loop após salvar os dados
        break

    except Exception as e:
        print(f"Erro ao obter ou salvar os dados: {e}")
