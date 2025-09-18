from random import randint
print('{:-^30}'.format('Jogo de Adivinhação'))
dif = 0
tentativas = 0
jogador = ''
while True:
    while dif == 0:
        print('DIFICULDADES:\n'
              '1 - Fácil\n'
              '2 - Médio\n'
              '3 - Difícil')
        dif = int(input('Escolha a Difículdade: '))
        if dif == 1:
            print('DIFICULDADE: Fácil \n'
                  'Acerte o número correto entre 1 á 10 com 5 tentativas. Boa Sorte!')
            computador = randint(1, 10)
            tentativas = 5
            jogador = int(input('Digite seu palpite: '))
            while jogador != computador:
                tentativas -= 1
                if jogador > computador:
                    print('MENOS...')
                else:
                    print('MAIS...')
                print(f'Você tem {tentativas} tentativas restantes.')
                print('-=' * 30)
                print('\n')
                jogador = int(input('Digite seu palpite: '))
                if tentativas == 0:
                    print('GAME OVER')
                    break
            if jogador == computador:
                print('PARABÉNS, VOCÊ GANHOU!!!')
                break
        elif dif == 2:
            print('DIFICULDADE: Médio \n'
                  'Acerte o número correto entre 1 á 50 com 7 tentativas. Boa Sorte!')
            tentativas = 7
            computador = randint(1, 50)
            jogador = int(input('Digite seu palpite: '))
            while jogador != computador:
                tentativas -= 1
                if jogador > computador:
                    print('MENOS...')
                else:
                    print('MAIS...')
                print(f'Você ainda tem {tentativas} tentativas restantes.')
                print('-=' * 30)
                print('\n')
                jogador = int(input('Digite seu palpite: '))
                if tentativas == 0:
                    print('GAME OVER')
                    break
            else:
                print('PARABÉNS, VOCÊ GANHOU!!!')
                break
        elif dif == 3:
            print('DIFICULDADE: Difícil \n'
                  'Acerte o número correto entre 1 á 100 com 10 tentativas. Boa Sorte!')
            tentativas = 10
            computador = randint(1,100)
            jogador = int(input('Digite seu palpite: '))
            while jogador != computador:
                tentativas -= 1
                if jogador > computador:
                    print('MENOS...')
                else:
                    print('MAIS...')
                print(f'Você ainda tem {tentativas} tentativas restantes.')
                print('-=' * 30)
                print('\n')
                jogador = int(input('Digite seu palpite: '))
                if tentativas == 0:
                    print('GAME OVER')
                    break
            else:
                print('PARABÉNS, VOCÊ GANHOU!!!')
                break