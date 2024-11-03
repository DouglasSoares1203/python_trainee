import tkinter as tk

class Calculadora:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")

        #Entrada de texto
        self.entry = tk.Entry(self.janela, width=35)
        self.entry.grid(row=0,column=0,columnspan=4)



if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()