frutas = ["laranja","maçã", "uva"]
print(frutas)
print(frutas[-1])
print(frutas[-3])
frutas = []
print(frutas)
letras = list("python")
print(letras)
numeros = list(range(10))
print(numeros)
carro = ["Ferrari", "F8",4200000,2020,2900,"São Paulo", True]
print(carro)


lista = ["p","y","t","h","o","n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])


# numeros = [1,30,21,2,9,65,34]
# pares = [numero for numero in numeros if numero % 2 ==0]


# numeros = [1,30,21,2,9,65,34]
# quadrado = []

# for numero in numeros:
#     quadrado.append(numeros**2)

# numeros = [1,30,21,2,9,65,34]
# quadrado = [numero ** 2 for numero in numeros]


lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

lista = [1, 'Python', [40, 30, 20]]
lista.copy()


l2 = lista.copy()

print(lista)

print(id(l2),id(lista))


l2[0] = 2

print(lista)
print(l2)


cores = ["vermelho","azul", "verde","azul"]

cores.count("vermelho")
cores.count("azul")
cores.count("verde")

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))



linguagens = ["python", "js", "c"]
print(linguagens)
linguagens.extend(["java","csharp"])
print(linguagens)


linguagens = ["python", "js", "c","java","csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))



linguagens = ["python", "js", "c","java","csharp"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))




linguagens = ["python", "js", "c","java","csharp"]
linguagens.remove("c")
print(linguagens)

linguagens = ["python", "js", "c","java","csharp"]
linguagens.reverse()
print(linguagens)



linguagens = ["python", "js", "c","java","csharp"]
linguagens.sort()
print(linguagens)

linguagens = ["python", "js", "c","java","csharp"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["python", "js", "c","java","csharp"]
linguagens.sort(key=lambda x:len(x))
print(linguagens)

linguagens = ["python", "js", "c","java","csharp"]
linguagens.sort(key=lambda x:len(x), reverse=True)
print(linguagens)

linguagens = ["python", "js", "c","java","csharp"]
print(len(linguagens))




linguagens = ["python", "js", "c","java","csharp"]
print(sorted(linguagens,key=lambda x:len(x)))

linguagens = ["python", "js", "c","java","csharp"]
print(sorted(linguagens,key=lambda x:len(x), reverse=True))