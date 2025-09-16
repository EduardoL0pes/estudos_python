##Opção01
# from random import randint
#
# print('\033[1;33m----Bem Vindo ao jogo de PAR ou ÍMPAR----\033[m')
# vit = 0
# while True:
#     print('\033[1;33m-=\033[m'*20)
#     play = int(input('Digite um número: '))
#     esc = input('Par ou Ìmpar [P/I]? ').upper().strip()
#     comp = randint(0, 10)
#     s = play + comp
#     print('\033[1;33m-=\033[m'*20)
#     if s % 2 == 0 and esc == 'P':
#         print('\033[1;32mVOCÊ VENCEU!\033[m')
#         vit += 1
#     elif s % 2 != 0 and esc == 'I':
#         print('\033[1;32mVOCÊ VENCEU!\033[m')
#         vit += 1
#     elif s % 2 == 0 and esc != 'P':
#         print('\033[1;31mVOCÊ PERDEU!\033[m')
#         print(f'Você jogou {play} e o computador {comp}. Total de {s} deu PAR')
#         break
#     else:
#         print('\033[1;31mVOCÊ PERDEU!\033[m')
#         print(f'Você jogou {play} e o computador {comp}. Total de {s} deu ÌMPAR')
#         break
# print(f'FIM DE JOGO!, VOCÊ VENCEU \033[1;32m{vit}\033[m VEZES.')

##Opção02
from random import randint

vit = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ìmpar? [P/I] ').strip().upper()[0]
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vit += 1
        else:
            print(f'Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vit += 1
        else:
            print(f'Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {vit} vezes.')