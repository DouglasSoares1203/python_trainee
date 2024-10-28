
# Etapa 1: Criar uma lista vazia chamada beatles
beatles = []

# Etapa 2: Adicionar membros iniciais à lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Membros Iniciais:")
print(beatles)

# Etapa 3: Solicitar ao usuário que adicione membros à lista
print("\nAdicione os seguintes membros:")
membros_adicionais = ["Stu Sutcliffe","Pete Best"]
for membro in membros_adicionais:
    beatles.append(membro)
    resposta = input(f"Deseja adicionar {membro} a lista? (s/n): ")
    if resposta.lower() != "s":
        beatles.remove(membro)
print("\nLista após adição de membros:")
print(beatles)

# Etapa 4: Remover membros da lista
membros_removidos = ["Stu Sutcliffe","Pete Best"]
for membro in membros_removidos:
    if membro in beatles:
        beatles.remove(membro)
print("\nLista após remoção de membros:")
print(beatles)

# Etapa 5: Adicionar Ringo Starr ao início da lista
beatles.insert(0,"Ringo Starr")
print("\nLista final:")
print(beatles)


#Esse programa demonstra as operações básicas com listas em Python:

#- append(): Adiciona um elemento ao final da lista.
#- insert(): Adiciona um elemento em uma posição específica da lista.
#- remove(): Remove a primeira ocorrência de um elemento na lista.
#- del: Remove um elemento em uma posição específica da lista.
