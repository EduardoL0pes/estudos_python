from random import randint
from time import sleep

dic = dict()
print('Valores sorteados:')

for j in range(1,5):
    nome_jogador = f"jogador{j}"
    num_dado = randint(1,6)
    dic[nome_jogador] = num_dado
    print(f'O jogador{j} tirou {num_dado}'.center(30))

ordem = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
print('Os vencedores são:')

cont = 0
for k, v in ordem.items():
    cont += 1
    sleep(1)
    print(f'{cont}° lugar: {k} com {v}'.center(30))