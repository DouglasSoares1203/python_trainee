def exibir_mensagem():
    print("Olá mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
    
def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="DG")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")








def calcular_total(numeros):
    return sum(numeros)


def retornar_antecessor_e_sucessor(numeros):
    antecessor = numeros - 1
    sucessor = numeros + 1
    return antecessor, sucessor



print(calcular_total([10,20,34]))
print(retornar_antecessor_e_sucessor(10))






def salvar_carro(marca,modelo,ano,placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","Palio",1999,"ABC-1234")
salvar_carro(marca="Fiat",modelo="Palio",ano=1999,placa="ABC-1234")
salvar_carro(**{"marca":"Fiat","modelo":"Palio","ano":1999,"placa":"ABC-1234"})




def exibir_poemas(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])

    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poemas("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)



def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def test(a,b):
    return a*2 + b*3


def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)
exibir_resultado(10,10,test)




salario = 2000

def salario_bonus(bonus,lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista_aux={lista_aux}")
    salario += bonus
    return salario


lista = [1]
novo_salario = salario_bonus(500, lista)
print(novo_salario)
print(lista)