nome = "python"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  olá mundo!  "
print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")


menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14,"#"))
print(menu.center(20,"#"))
print("p-y-t-h-o-n")
print("-".join(menu))


for letra in menu:
    print(letra , end="-")

print()

print("-".join(menu))





nome = "DG"
idade  = 35
profissao = "Programador"
linguagem = "Python"
saldo = 8.000

dados = {"nome": "DG", "idade": 35}

print("Nome: %s Idade: %d" %(nome,idade))
print("Nome: {} Idade: {}".format(nome,idade))
print("Nome: {0} Idade: {1}".format(nome,idade))
print("Nome: {0} Idade: {1} Nome: {0} {0}".format(nome,idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))


print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")




nome = "Douglas Aquino Soares"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])







nome = "DG"

mensagem = f"""
    Olá meu nome é {nome}
  Estou aprendendo Python
    Essa mensagem tem diferentes recuos.
 """


print(mensagem)


print(""" 
    ========= MENU =========
      

    1 - Depositar
    2 - Sacar
    0 - Sair
 
    ========================
      
      Obrigado por usar nosso sistema!!!!
      
""")

