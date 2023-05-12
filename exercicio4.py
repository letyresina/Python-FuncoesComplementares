'''
    Crie uma função chamada bhaskara que receba 3 valores (a, b, c) e calcule as raízes da fórmula
    de Bhāskara.Faça um teste com bhaskara(1, -4, -5)e a função deve exibir as raízes: 5.0 e -1.0.
'''

import math

def bhaskara(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(f"A primeira raiz é {x1} e a segunda raiz é de {x2}")

try:
    a = float(input("Informe um número qualquer: "))
    b = float(input("Informe um número qualquer: "))
    c = float(input("Informe um número qualquer: "))

    bhaskara(a, b, c)
except ValueError:
    print(f"Por favor, digite um valor válido!")