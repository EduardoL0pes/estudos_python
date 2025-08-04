from random import randint

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
        palpite = int(input('Você \033[1;31m[ERROU]\033[m Tente novamente: '))
        palpites += 1
        if num == palpite:
            print(f'Parabens você \033[1;32mACERTOU!\033[m Com \033[1:32m{palpites}\033[m palpites.')