from random import randint

print('{:-^31}'.format(' Jogo de Adivinhação 2.0 '))

while True:
    print('DIFICULDADES:\n'
          '1 - Fácil\n'
          '2 - Médio\n'
          '3 - Difícil')
    dif = int(input('Escolha a Dificuldade: '))
    if dif == 1:
        limite = 10
        tentativa = 5
        print('DIFICULDADE: Fácil\n Acerte o número correto entre 1 e 10 com 5 tentativas. Boa Sorte!')
    elif dif == 2:
        limite = 50
        tentativa = 7
        print('DIFICULDADE: Médio\n Acerte o número correto entre 1 e 50 com 7 tentativas. Boa Sorte!')
    elif dif == 3:
        limite = 100
        tentativa = 7
        print('DIFICULDADE: Difícil\n Acerte o número correto entre 1 e 100 com 10 tentativas. Boa Sorte!')
    else:
        print('Opção inválida. Tente novamente')
        print()
        continue
    computador = randint(1, limite)
    jogador = int(input('Digite seu palpite: '))
    while jogador != computador > 0:
        tentativa -= 1
        if jogador > computador:
            print('MENOS...')
        else:
            print('MAIS...')
        if tentativa > 0:
            print(f'Você ainda tem {tentativa} tentativas restantes.')
            print('-='*30)
            print()
            jogador = int(input('Digite seu palpite: '))
        else:
            print('GAME OVER! O número era', computador)
    if jogador == computador:
        print('PARABÉNS, VOCÊ VENCEU!!!')
    break