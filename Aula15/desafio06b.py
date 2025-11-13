time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()

    jogador['nome'] = input('Nome do jogador: ').title().strip()
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp in 'SN':
            break
        print('ERRO! Responda somente S ou N.')
    if resp == 'N':
        break

print('-='*30)
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for i, j in enumerate(time):
    print(f'{i:<4}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('PROGRAMA FINALIZADO!')