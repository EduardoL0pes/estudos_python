numeros = []
for n in range(0, 8):
    numeros.append(int(input(f'Digite {n+1}° valor: ')))
print(f'Lista completa: {numeros}')

print('Números pares:', end=' ')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')

print()

print('Números ímpares:', end=' ')
for num in numeros:
    if num % 2 == 1:
        print(num, end=' ')