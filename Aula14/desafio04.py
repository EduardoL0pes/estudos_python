matriz = []
soma  = 0
soma_col3 = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite um valor [{i}, {j}]: '))
        linha.append(valor)

        if valor % 2 == 0:
            soma += valor

    matriz.append(linha)

for linha in matriz:
    print(linha)
    soma_col3 += linha[2]

maior = matriz[1][0]
for c in matriz[1]:
    if c > maior:
        maior = c

print('-='*30)
print(f'A soma de todos os valores pares da matriz é igual á: {soma}.')
print(f'A soma dos valores da terceira coluna é: {soma_col3}.')
print(f'O maior valor da segunda linha é {maior}.')

