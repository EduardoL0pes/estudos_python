jogador = dict()
gols = []
tot_gols = 0

while True:
    jogador['nome'] = input('Nome do Jogador: ').title()
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    for i in range(partidas):
        gols_marcados = int(input(f'Quantos gols na partida {i+1}? '))
        tot_gols += gols_marcados
        gols.append(gols_marcados)

    jogador['gols'] = gols[:]
    jogador['total'] = tot_gols

    resp = input('Deseja continuar? [S/N]: ').upper()
    print('-'*30)

    if resp in 'N':
        break

print(jogador)