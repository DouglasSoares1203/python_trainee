class Bicicleta:
    def __init__(self, cor,moddelo,ano,valor):

        self.cor = cor
        self.modelo = moddelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim")

    def parar(self):
        print("Parando Bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm...")


    def get_cor(self):
        return self.cor
    
    # def __str__(self):
    #     return f"bicicleta {self.cor}, {self.modelo}, {self.ano}, {self.valor}, valor = {self.valor}"



b1 = Bicicleta("Vermelha", "caloi",2022,600)

# b1.buzinar()
# b1.correr()
# b1.parar()



print(b1.cor, b1.modelo, b1.ano, b1.valor)

def __str__(self):
    return f"{self.__class__.__name__} : {", ".join([f'{chave}={valor}' for chave, valor 
    in self.__dict__.item()])}"



b2 = Bicicleta("Verde", "monark", 2000,189)
Bicicleta.buzinar(b2)
print(b2.get_cor())

print(b2)



class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()



































































































































































