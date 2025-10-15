dado = list()
pessoas = list()
tot_cad = 0
while True:
    dado.append(input('Digite seu nome: ').strip())
    dado.append(int(input('Peso: ')))
    tot_cad += 1

    pessoas.append(dado[:])
    dado.clear()

    resp = input('Deseja continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break

mais_pesadas = []
mais_leves = []
max_peso = min_peso = 0

for p in pessoas:
    if p[1] >= 100:
        mais_pesadas.append(p[0])
        if p[1] > max_peso:
            max_peso = p[1]
    elif p[1] <= 70:
        mais_leves.append(p[0])
        min_peso = p[1]
        if p[1] < min_peso:
            min_peso = p[1]

print(f'Ao todo, você cadastrou {tot_cad} pessoas.')
print(f'O maior peso foi de {max_peso}Kg. Peso de {mais_pesadas}')
print(f'O menor peso foi de {min_peso}Kg. Peso de {mais_leves}')
