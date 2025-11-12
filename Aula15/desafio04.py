jogador = {
    'nome': input('Nome do jogador: ').title().strip()
}

gols = []
tot = 0

partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for p in range(partidas):
    gols_partidas = int(input(f'Quantos gols na partida {p+1}? '))
    tot += gols_partidas
    gols.append(gols_partidas)

    jogador['gols'] = gols[:]
    jogador['total'] = tot
print('-'*30)

for keys, values in jogador.items():
    print(f'O campo {keys} tem o valor de {values}.')
print('-'*30)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print(f'  => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {tot} gols.')