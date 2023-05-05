'''
    Crie uma função que receba três números como parâmetros, e retorne True se a soma de quaisquer 
    pares de números gera a soma do terceiro número. Caso contrário retorne False.
'''

def tresNumeros(num1, num2, num3):
    if (num1 + num2 == num3):
        return True
    else:
        return False

num1 = int(input("Informe um número inteiro qualquer: "))

num2 = int(input("Informe um número inteiro qualquer: "))

num3 = int(input("Informe um número inteiro qualquer: "))

if tresNumeros(num1, num2, num3) == True:
    print(f"A soma entre {num1} e {num2} é igual à {num3}")
else:
    print(f"A soma entre {num1} + {num2} não é igual à {num3}")