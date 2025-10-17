from random import randint
from time import sleep

print('-'*25)
print('JOGO DA MEGA SENA'.center(25))
print('-'*25)

quantidade = int(input('Quantos jogos deseja gerar? '))
print()
print(f'GERANDO {quantidade} JOGOS'.center(30, '='))
sleep(1)

todos_jogos = []
for _ in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    todos_jogos.append(jogo)

for i, j in enumerate(todos_jogos):
    sleep(0.5)
    print(f'jogo {i+1}: {j}')