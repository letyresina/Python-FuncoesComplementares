'''
    Em um jogo de dados, pode ser sorteado qualquer número entre 1 e 6. Faça uma função que simule
    1 milhão de lançamentos de dados e mostre quantas vezes cada número foi sorteado.
'''
import random;

def sorteio():
    for a, b, c, d, e, f in range(1, 1001):
        num = random.randint(1,6)
        i += 1
        print(num)

sorteio()

