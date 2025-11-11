from random import randint
from time import sleep
from operator import itemgetter

dic = dict()
print('Valores sorteados:')

for j in range(1,5):
    nome_jogador = f"jogador{j}"
    num_dado = randint(1,6)
    dic[nome_jogador] = num_dado
    print(f'O jogador{j} tirou {num_dado}'.center(30))

# ordem = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
ordem = list(sorted(dic.items(), key=itemgetter(1), reverse=True))
print('Ranking dos jogadores são:')

for k, v in enumerate(ordem):
    sleep(1)
    print(f'{k+1}° lugar: {v[0]} com {v[1]}'.center(30))