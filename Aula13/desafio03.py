valores = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    valores.append(num)

for i in range(len(valores)):
    menor_indice = i

    for v in range(i + 1, len(valores)):
        if valores[v] < valores[menor_indice]:
            menor_indice = v

    valores[i], valores[menor_indice] = valores[menor_indice], valores[i]

print('Lista Ordenada: ', valores)