from random import choice
print('-=-='*10)
print('\033[1;33mVamos Jogar JOKENPO\033[m')
print('-=-='*10)
jogador = input('Digite sua escolha: ')
jokenpo = 'pedra', 'papel', 'tesoura'
gerador = choice(jokenpo)
if gerador == jogador:
    print('EMPATE! Por favor tente novamente! {} DRAW {}'.format(jogador, gerador))
    print('\033[1;33mFIM DE JOGO!!!\033[m')
elif jogador == 'papel' and gerador == 'pedra':
    print('Parabéns você venceu! {} ganha de {}'.format(jogador, gerador))
elif jogador == 'pedra' and gerador == 'tesoura':
    print('Parabéns você venceu! {} ganha de {}'.format(jogador, gerador))
elif jogador == 'tesoura' and gerador == 'papel':
    print('Parabéns você venceu! {} ganha de {}'.format(jogador, gerador))
else:
    print('Você perdeu :/ {} ganha de {}'.format(gerador, jogador))
    print('\033[1;33mFIM DE JOGO!!!\033[m')
