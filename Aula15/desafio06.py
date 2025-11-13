jogadores_dic = {}
jogadores_lista = []

while True:
    jogadores_dic['jogador'] = input('Nome do jogador: ').title().strip()

    resp = input('Deseja continuar? [S/N] ').upper()
    if resp == 'N':
        break

print(jogadores_dic)