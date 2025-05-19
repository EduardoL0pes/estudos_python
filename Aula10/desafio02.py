from random import randint

num = randint(0,10)
palpites = ''
print('Jogo de adivinha')
while num != palpite:
        palpite = int(input('Digite um número entre 0 á 10: '))
    if num == palpite:
        print('Parabéns você acertou!')
    else:
        print('Você Errou, tente novamente.')
print('fim')
