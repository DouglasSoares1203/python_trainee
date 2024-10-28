"""
Este módulo contém exercícios relacionados à tomada de decisão no Python.
Ele abrange exemplos de uso de estruturas condicionais como if, elif, e else.
"""

income = float(input("Entre com os rendimentos "))

if income < 85528:
    tax = income * 0.18 - 556.02
    # Escrever o resto do código aqui.
    tax = round(tax, 0
    )

    print(
    "A taxa é:", tax, "thalers")
