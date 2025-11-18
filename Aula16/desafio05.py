from random import randint
from time import sleep

list_num = []
def sorteio():
    print('Sorteando 5 valores da lista: ', end='')

    for n in range(5):
        num = randint(1,10)
        list_num.append(num)
        print(f'{num}', end=' ')
        sleep(0.3)
    print()

def soma_par():
    soma = 0
    for p in list_num:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores PARES de {list_num}, temos {soma}')

sorteio()
soma_par()