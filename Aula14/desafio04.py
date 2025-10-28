# matriz = []
# soma  = 0
# soma_col3 = 0
# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f'Digite um valor [{i}, {j}]: '))
#         linha.append(valor)
#
#         if valor % 2 == 0:
#             soma += valor
#
#     matriz.append(linha)
#
# for linha in matriz:
#     print(linha)
#     soma_col3 += linha[2]
#
# maior = matriz[1][0]
# for c in matriz[1]:
#     if c > maior:
#         maior = c
#
# print('-='*30)
# print(f'A soma de todos os valores pares da matriz é igual á: {soma}.')
# print(f'A soma dos valores da terceira coluna é: {soma_col3}.')
# print(f'O maior valor da segunda linha é {maior}.')
#

#Opção02
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai_l2 = scol3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l},{c}]: '))

print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)

print(f'A soma de todos os valores pares: {spar}')

for l in range(0, 3):
    scol3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna: {scol3}')

for c in range(0, 3):
    if c == 0:
        mai_l2 = matriz[1][c]
    else:
        mai_l2 = matriz[1][c]
print(f'O maior valor da segunda linha: {mai_l2}')