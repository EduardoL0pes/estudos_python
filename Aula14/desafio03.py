# matriz = []
#
# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f'Digite um valor [{i}, {j}]: '))
#         linha.append(valor)
#     matriz.append(linha)
#
# for linha in matriz:
#     print(*linha)        # * Desempacota a lista, mostrando sem os conchetes e as virgulas
#     #print(linha)


# Opção02
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor {l, c}: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
