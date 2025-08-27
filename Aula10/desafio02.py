#Opção 1
"""from random import randint

num = ''
palpite = ''
palpites = 1
print('\033[1;33m----Jogo de Adivinha----\033[m')
while num == '':
    num = randint(1,10)
    palpite = int(input('Digite um número entre 0 á 10: '))
    if num == palpite:
        print('Parabéns você \033[1;32mACERTOU!\033[m \nNossa.. e de primeira, Sortudo!!')
    while num != palpite:
        if num > palpite:
            palpite = int(input('Mais.. Tente novamente: '))
            palpites += 1
        else:
            palpite = int(input('Menos.. Tente novamente: '))
            palpites += 1
        if num == palpite:
            print(f'Parabens você \033[1;32mACERTOU!\033[m Com \033[1:32m{palpites}\033[m palpites.')"""

#Opção 2
from random import randint
computador = randint(0,10)
print('\033[1;34mJogo de adivinha\033[m')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com \033[1;34m{palpites}\033[m tentativas. Parabéns!')