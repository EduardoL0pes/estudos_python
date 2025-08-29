#Opção1
# numero = int(input('Digite um número: '))
# fatorial = 1
# if numero < 0:
#     print('Não é possível calcular o fatorial de um número negativo.')
# elif numero == 0:
#     print('O fatorial de 0 é 1.')
# else:
#     while numero > 0:
#         fatorial = fatorial * numero  # loop1 5, loop2 20, loop3 60, loop4 120, loop5 120.
#         numero -= 1  # decrementando
# print(f'O fatorial é {fatorial}.')


#Opção2
# from math import factorial
#
# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

#Opção3
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {c}! = ',end='')
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')