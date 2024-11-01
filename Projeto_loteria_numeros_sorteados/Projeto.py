# import random

# def gerar_numeros_loteria():
#     return random.sample(range(1,61),6)

# numeros = gerar_numeros_loteria()
# print("Números da loteria: ")
# print(sorted(numeros))

import random
import tkinter as tk

class LoteriaApp:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Loteria")
        self.janela.geometry("300x200")
        self.label = tk.Label(self.janela, text="Clique para gerar números")

        self.label.pack()
        self.botao = tk.Button(self.janela,text="Gerar", command=self.gerar_numeros)
        self.botao.pack()

    def gerar_numeros(self):
            numeros = random.sample(range(1,61),6)
            self.label.config(text="Números da loteria:  " + str(sorted(numeros)))

    def run(self):
                self.janela.mainloop()

if __name__ == "__main__":
                app = LoteriaApp()
                app.run()


#         Nesse código:

# - (link unavailable)() cria a janela principal do aplicativo.
# - self.janela.title("Loteria") define o título da janela.
# - tk.Label e tk.Button criam o rótulo e o botão na janela.
# - pack() organiza os elementos na janela.
# - mainloop() inicia o loop principal do aplicativo.

# Execute esse código para criar o aplicativo de loteria!