from time import sleep
jogador_dic = {}
jogadores_lista = []
gols = []

while True:
    jogador_dic.clear()
    gols.clear()

    jogador_dic['jogador'] = input('Nome do jogador: ').title().strip()
    partidas = int(input(f'Quantas partidas {jogador_dic['jogador']} jogou? '))

    for c in range(partidas):
        gols_partida = int(input(f'  Quantos gols na partida {c+1}? '))
        gols.append(gols_partida)
    jogador_dic['gols'] = gols[:]

    jogadores_lista.append(jogador_dic.copy())

    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp in 'SN':
            break
        print('ERRO! Responda somente S ou N.')
    if resp == 'N':
        break

print('-='*35)
print(f'{"Cod.":<5}{"Nome":<10}{"Gols":<12}{"Total":<5}')
print('-'*36)

for j, g in enumerate(jogadores_lista):
    print(f'{j:<4}{g['jogador']:<10}{g['gols']}{sum(g['gols']):>7}')
print('-'*36)

while True:
    opc = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if opc == 999:
        break

    if opc >= len(jogadores_lista):
        print(f'ERRO! Não existe jogador com código {opc}!')
    else:
        print(f'  --LEVANTAMENTO DO JOGADOR {jogadores_lista[opc]['jogador']}:')
        for p, g in enumerate(jogadores_lista[opc]['gols']):
            print(f'    No jogo {p+1} fez {g} gols.')
        print('-'*36)

print('ENCERRANDO...')
sleep(1)
print('PROGRAMA FINALIZADO!')