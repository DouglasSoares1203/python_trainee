import csv
import os
import random
from datetime import datetime, timedelta

# Função para gerar dados fictícios para diferentes tipos de relatório
def gerar_dados(tipo, num_linhas=100):
    dados = []
    data_inicial = datetime(2023, 1, 1)
    
    if tipo == 'Logística':
        for _ in range(num_linhas):
            dados.append([
                random.randint(1000, 9999),  # ID Pedido
                (data_inicial + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d'),  # Data
                random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']),  # Local
                random.choice(['Transportadora X', 'Transportadora Y']),  # Transportadora
                round(random.uniform(100.0, 5000.0), 2),  # Valor do pedido
                random.choice(['Entregue', 'Em trânsito', 'Aguardando']),  # Status
                random.randint(1, 100),  # Quantidade
                round(random.uniform(1.0, 50.0), 2),  # Peso (kg)
                random.randint(1, 10),  # Dias de entrega
                random.choice(['Sim', 'Não'])  # Entrega Prioritária
            ])
    elif tipo == 'RH':
        for _ in range(num_linhas):
            dados.append([
                random.randint(100, 999),  # ID Funcionário
                random.choice(['João', 'Maria', 'Carlos', 'Ana', 'Fernanda']),  # Nome
                random.choice(['Vendas', 'TI', 'Administração', 'Operações']),  # Departamento
                random.randint(18, 65),  # Idade
                random.choice(['Masculino', 'Feminino', 'Outro']),  # Gênero
                round(random.uniform(2000.0, 15000.0), 2),  # Salário
                random.randint(0, 30),  # Dias de férias
                random.choice(['Sim', 'Não']),  # Treinamento realizado
                random.choice(['Efetivo', 'Temporário', 'Estagiário']),  # Tipo de contrato
                random.randint(0, 20)  # Anos na empresa
            ])
    elif tipo == 'Loja de Veículos':
        for _ in range(num_linhas):
            dados.append([
                random.randint(10000, 99999),  # ID Veículo
                random.choice(['Sedan', 'SUV', 'Caminhão', 'Motocicleta']),  # Tipo
                random.choice(['Marca A', 'Marca B', 'Marca C']),  # Marca
                random.choice(['Modelo X', 'Modelo Y', 'Modelo Z']),  # Modelo
                random.randint(2000, 2023),  # Ano
                round(random.uniform(20000.0, 200000.0), 2),  # Preço
                random.choice(['Novo', 'Usado']),  # Condição
                random.randint(0, 200000),  # Quilometragem
                random.choice(['Gasolina', 'Diesel', 'Elétrico']),  # Combustível
                random.choice(['Disponível', 'Vendido'])  # Status
            ])
    return dados

# Função para criar o arquivo CSV no diretório especificado
def criar_csv(nome_arquivo, cabecalhos, dados):
    # Definir o caminho para o diretório desejado
    pasta_destino = os.path.join('relatorio_BI', 'informação')
    
    # Criar o diretório se ele não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Caminho completo do arquivo
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)

    # Criar e salvar o arquivo CSV
    with open(caminho_completo, mode='w', newline='', encoding='utf-8') as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(cabecalhos)  # Cabeçalhos
        escritor_csv.writerows(dados)

    print(f'Arquivo salvo em: {os.path.abspath(caminho_completo)}')

# Menu para o usuário escolher o tipo de relatório
def main():
    print("Escolha o tipo de relatório que deseja gerar:")
    print("1. Logística")
    print("2. RH")
    print("3. Loja de Veículos")
    opcao = input("Digite o número da sua escolha: ")

    if opcao == '1':
        tipo = 'Logística'
        cabecalhos = ['ID Pedido', 'Data', 'Local', 'Transportadora', 'Valor do Pedido',
                      'Status', 'Quantidade', 'Peso (kg)', 'Dias de Entrega', 'Entrega Prioritária']
    elif opcao == '2':
        tipo = 'RH'
        cabecalhos = ['ID Funcionário', 'Nome', 'Departamento', 'Idade', 'Gênero',
                      'Salário', 'Dias de Férias', 'Treinamento Realizado', 'Tipo de Contrato', 'Anos na Empresa']
    elif opcao == '3':
        tipo = 'Loja de Veículos'
        cabecalhos = ['ID Veículo', 'Tipo', 'Marca', 'Modelo', 'Ano', 'Preço', 'Condição',
                      'Quilometragem', 'Combustível', 'Status']
    else:
        print("Opção inválida. Tente novamente.")
        return

    # Gerar dados e criar o arquivo CSV
    dados = gerar_dados(tipo, num_linhas=200)
    nome_arquivo = f'relatorio_{tipo.lower().replace(" ", "_")}.csv'
    criar_csv(nome_arquivo, cabecalhos, dados)

# Executa o programa
if __name__ == '__main__':
    main()
