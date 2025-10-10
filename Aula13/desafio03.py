lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #Se ele for igual a 0 ou 'n' menor que o último número da lista
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')


# valores = []
# for c in range(0, 5):
#     num = int(input('Digite um valor: '))
#     valores.append(num)
#
# for i in range(len(valores)):
#     menor_indice = i
#
#     for v in range(i + 1, len(valores)):
#         if valores[v] < valores[menor_indice]:
#             menor_indice = v
#
#     valores[i], valores[menor_indice] = valores[menor_indice], valores[i]
#
# print('Lista Ordenada: ', valores)