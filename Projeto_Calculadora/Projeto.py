import tkinter as tk

class Calculadora:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")

        #Entrada de texto
        self.entry = tk.Entry(self.janela, width=35)
        self.entry.grid(row=0,column=0,columnspan=4)

        #Botões
        self.botao1 = tk.Button(self.janela, text="1", command=lambda: self.clique("1"))
        self.botao1.grid(row=1, column=0)
        self.botao2 = tk.Button(self.janela, text="2", command=lambda: self.clique("2"))
        self.botao2.grid(row=1, column=1)
        self.botao3 = tk.Button(self.janela, text="3", command=lambda: self.clique("3"))
        self.botao3.grid(row=1, column=2)

        self.botao_soma = tk.Button(self.janela, text="+", command=lambda: self.clique("+"))
        self.botao_soma.grid(row=1, column=3)

        self.botao4 = tk.Button(self.janela, text="4", command=lambda: self.clique("4"))
        self.botao4.grid(row=2, column=0)
        self.botao5 = tk.Button(self.janela, text="5", command=lambda: self.clique("5"))
        self.botao5.grid(row=2, column=1)
        self.botao6 = tk.Button(self.janela, text="6", command=lambda: self.clique("6"))
        self.botao6.grid(row=2, column=2)

        self.botao_subtracao = tk.Button(self.janela, text="-", command=lambda: self.clique("-"))
        self.botao_subtracao.grid(row=2, column=3)

        self.botao7 = tk.Button(self.janela, text="7", command=lambda: self.clique("7"))
        self.botao7.grid(row=3, column=0)
        self.botao8 = tk.Button(self.janela, text="8", command=lambda: self.clique("8"))
        self.botao8.grid(row=3, column=1)
        self.botao9 = tk.Button(self.janela, text="9", command=lambda: self.clique("9"))
        self.botao9.grid(row=3, column=2)

        self.botao_multiplicacao = tk.Button(self.janela, text="*", command=lambda: self.clique("*"))
        self.botao_multiplicacao.grid(row=3, column=3)

        self.botao0 = tk.Button(self.janela, text="0", command=lambda: self.clique("0"))
        self.botao0.grid(row=4, column=0)
        self.botao_ponto = tk.Button(self.janela, text=".", command=lambda: self.clique("."))
        self.botao_ponto.grid(row=4, column=1)
        self.botao_igual = tk.Button(self.janela, text="=", command=self.calcula)
        self.botao_igual.grid(row=4, column=2)

        self.botao_divisao = tk.Button(self.janela, text="/", command=lambda: self.clique("/"))
        self.botao_divisao.grid(row=4, column=3)

    def clique(self,valor):
        self.entry.insert(tk.END, valor)

    def calcula(self):
        try:
            resultado = eval(self.entry.get())
            self.entry.delete(0,tk.END)
            self.entry.insert(tk.END, str(resultado))
        except Exception as e:
            self.entry.delete(0,tk.END)
            self.entry.insert(tk.END, "Erro")

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()