def ficha(nome='', gols=0):
    global n, gol

    if n == '' and gol < 0:
        print(f'O jogador <Desconhecido> fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador <{nome}> fez {gols} gol(s) no campeonato.')

n = input('Nome do jogador: ')
gol = int(input('Quantos gols? '))

ficha(nome=n, gols=gol)