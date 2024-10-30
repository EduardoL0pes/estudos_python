from random import choice
from time import sleep

print('-=-='*10)
print('{:^40}'.format('Vamos jogar JOKENPÔ'))
print('-=-='*10)
print('''Escolha uma das Opções...
[ 1 ] Papel
[ 2 ] Tesoura
[ 3 ] Pedra ''')
computador = 'papel', 'tesoura', 'pedra'
gerador = choice(computador)
jogador = int(input('Digite sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
if jogador == 1 and gerador == 'pedra':
    print('\033[1;32mJOGADOR VENCEU!!')
elif jogador == 2 and gerador == 'papel':
    print('\033[1;32mJOGADOR VENCEU!!')
elif jogador == 3 and gerador == 'tesoura':
    print('\033[1;32mJOGADOR VENCEU!!')
elif jogador == 1 and gerador == 'papel' or jogador == 2 and gerador == 'tesoura' or jogador == 3 and gerador == 'pedra':
    print('\033[1;33m Houve um EMPATE!\033[m')
else:
    print('\033[1;31mJOGADOR PERDEU :/\033[m')
