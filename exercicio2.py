'''
    Dizemos que um número natural é triangular se ele é produto de três números naturais 
    consecutivos. Por exemplo: 120 é triangular, pois 4 * 5 * 6 = 120. 
    2730 é triangular, pois 13 * 14 * 15 = 2730. Faça uma função que receba um número inteiro e 
    retorne True se for um número triangular e False, caso contrário.
'''

# ler esse site https://mundoeducacao.uol.com.br/matematica/numeros-triangulares.htm#:~:text=Portanto%2C%20os%20n%C3%BAmeros%20triangulares%20podem,1%20e%20primeiro%20termo%201. para fazer


def triangular(num):
    if type(num) != 0 and num < 0:
        raise TypeError("O número deve ser natural.")

    for i in range(num):
        if i * (i+1) * (i+2) == num:
            return True
    return False

try:
    numero = int(input("Informe um número inteiro: "))
    if triangular(numero) == True:
        print(f"O número {numero} é triangular!")
    else:
        print(f"O número {numero} não é triangular!")
except ValueError:
    print("O valor informado não é inteiro! Tente novamente!")
except TypeError as erro:
    print(f"{erro}")
