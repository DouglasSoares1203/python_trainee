# Dicionário com opções de custos de casa
opcoes_custos = {
    1: "Aluguel",
    2: "Contas de água",
    3: "Contas de luz",
    4: "Contas de gás",
    5: "Internet",
    6: "TV por assinatura",
    7: "Seguro",
    8: "Manutenção"
}

# Dicionário para armazenar custos escolhidos
custos_casa = {}

def imprimir_opcoes():
    print("Escolha os custos de casa:")
    for codigo, descricao in opcoes_custos.items():
        print(f"{codigo} - {descricao}")

# Função para calcular soma total
def calcular_soma_total(custos):
    soma_total = sum(custos.values())
    return soma_total

# Programa principal
imprimir_opcoes()

while True:
    escolha  = input("Digite o código do custo (ou 's' para sair)")

    if escolha.lower() == 's':
        break

    try: 
        escolha = int(escolha)
        if escolha in opcoes_custos:
            valor = float(input(f"Digite o valor do{opcoes_custos[escolha]}: R$"))
            custos_casa[opcoes_custos[escolha]] = valor
        else:
            print("Código inválido.")
    except ValueError:
            print("Entrada inválida")

# Imprimir custos de casa
print("\nCustos de Casa")
for custo, valor in custos_casa.items():
    print(f"{custo}: R${valor:.2f}")


# Calcular e imprimir soma total
soma_total = calcular_soma_total(custos_casa)
print(f"\nSoma Total: R${soma_total:.2f}")