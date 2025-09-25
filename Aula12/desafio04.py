num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))
num_tup = num, num2, num3, num4

print(f'Você digitou os valores {num_tup}')
if num_tup.count(9):
    print(f'O valor 9 foi digitado {num_tup.count(9)} vezes.')
else:
    print(f'O valor 9 foi digitado 0 vezes.')
if 3 in num_tup:
    print(f'O valor 3 foi digitado na posição {num_tup.index(3)+1}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
pares = tuple(x for x in num_tup if x % 2 == 0)
print(f'Números pares são: {pares}')
