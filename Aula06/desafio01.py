import random

num = random.randint(0, 5)
res = int(input('Digite o valor: '))
if res == num:
    print('Parabéns você acertou!!')
else:
    print('Você perdeu :p')
    print('A resposta certa é {}'.format(num))

print('Fim de Jogo')