from random import choice
print('-=-='*10)
print('\033[1;33mVamos Jogar JOKENPO\033[m')
print('-=-='*10)
jogador = input('Digite sua escolha: ')
jokenpo = 'pedra', 'papel', 'tesoura'
gerador = choice(jokenpo)
if jogador == gerador:
    print('Parabéns você VENCEU!!')
else:
    print('Computador venceu, \033[1;31m{}\033[m ganha de \033[1;31m{}\033[m.'.format(gerador, jogador))
