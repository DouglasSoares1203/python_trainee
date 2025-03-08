print(set([1,2,3,1,3,4]))
print(set("abacaxi"))
print(set(("palio","gol","celta","palio")))


linguagens = {"python","java","python"}
print(linguagens)


numeros = {1,2,3,2}
numeros = list(numeros)
print(numeros[0])



conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.union(conjunto_b)
conjunto_a.intersection(conjunto_b)
conjunto_a.difference(conjunto_b)
conjunto_a.symmetric_difference(conjunto_b)
conjunto_b.difference(conjunto_a)




conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)


conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)


sorteio = {1,23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

sorteio
sorteio.clear()
sorteio

sorteio
sorteio.copy()
sorteio


numeros = {1,2,3,1,2,3,4,5,5,6,7,8,9,0}

numeros
numeros.discard(1)
numeros.discard(45)
numeros


print(numeros)
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros)


numeros = {1,2,3,1,2,3,4,5,5,6,7,8,9,0}

print(numeros)
print(numeros.remove(0))
print(numeros)


numeros = {1,2,3,1,2,3,4,5,5,6,7,8,9,0}
len(numeros)




numeros = {1,2,3,1,2,3,4,5,5,6,7,8,9,0}
1 in numeros
10 in numeros
