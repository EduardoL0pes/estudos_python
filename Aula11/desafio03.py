from random import randint

print('\033[1;33m----Bem Vindo ao jogo de PAR ou ÍMPAR----\033[m')
vit = 0
while True:
    print('\033[1;33m-=\033[m'*20)
    play = int(input('Digite um número: '))
    esc = input('Deseja escolher [P/I]? ').upper().strip()
    comp = randint(1, 10)
    s = play + comp
    print('\033[1;33m-=\033[m'*20)
    if s % 2 == 0 and esc == 'P':
        print('\033[1;32mVOCÊ GANHOU!\033[m')
        vit += 1
    else:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
        break
print(f'FIM DE JOGO!, VOCÊ GANHOU \033[1;32m{vit}\033[m VEZES.')

print(f'computador {comp}')
print(f'Player {play}')
