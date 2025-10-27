# numeros = []
# for n in range(0, 7):
#     numeros.append(int(input(f'Digite {n+1}° valor: ')))
# print(f'Lista completa: {numeros}')
#
# num_ordem_p = []
# for num in numeros:
#     if num % 2 == 0:
#         num_ordem_p.append(num)
#
# num_ordem_p.sort()
# print(f'Números pares: {num_ordem_p}')
#
# num_ordem_i = []
# for num in numeros:
#     if num % 2 == 1:
#         num_ordem_i.append(num)
#
# num_ordem_i.sort()
# print(f'Números ímpares: {num_ordem_i}')


# Opção02
numeros = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite {n+1}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f'Pares: {sorted(numeros[0])}')
print(f'Ímpares: {sorted(numeros[1])}')

