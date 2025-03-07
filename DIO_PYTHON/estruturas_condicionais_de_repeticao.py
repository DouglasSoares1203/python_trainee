def sacar(valor):
    saldo = 500


    if saldo >= valor:
        print("valor sacado")
        print("Retire o seu dinheiro na boca do caixa")


    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 100
    saldo >= valor

sacar(1000)



MAIOR_IDADE = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe a idade!: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade , pode tirar o CNH")


if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade , pode tirar o CNH")
else:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade , pode tirar o CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas téoricas, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar a CNH")



conta_normal = False
conta_universitaria = False
conta_especial = True
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada:")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente")






saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")




texto = input ("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:

    print()
    print("Executa no final do laço")



for numero in range(0,51,5):
    print(numero,end="")



opcao = -1

while opcao !=0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

else:
    print("Obrigado por usar nosso sistema bancário, até a próxima")





while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    print(numero)

print("Acertou MIZERAVI é 10!")




for numero in range(100):
    if numero == 10:
        break
    print(numero,end=" ")
    
    
for numero in range(100):
    if numero == 10:
        continue
    print(numero,end=" ")



for numero in range(100):

    if numero % 2 == 0:
        continue
    print(numero,end=" ")
