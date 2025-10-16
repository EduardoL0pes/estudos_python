matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite um valor [{i}, {j}]: '))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(*linha)        # * Desempacota a lista, mostrando sem os conchetes e as virgulas
    #print(linha)

