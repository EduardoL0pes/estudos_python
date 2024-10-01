from random import randint
from time import sleep

num = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...') #computador
res = int(input('Digite o valor: ')) #jogador
print('PROCESSANDO...') #tempo de processamento obs:somente estético
sleep(2) #tempo de processamento obs:somente estético
if res == num:
    print('Parabéns você acertou!!')
else:
    print('Você perdeu :p')
    print('A resposta certa é {}'.format(num))

print('Fim de Jogo...')