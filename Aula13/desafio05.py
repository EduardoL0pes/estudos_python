# valores = []
# num_par = []
# num_impar = []
# while True:
#     for c in range(0, 2):
#         num = int(input('Digite um valor: '))
#         valores.append(num)
#
#         if num % 2 == 0:
#             num_par.append(num)
#         else:
#             num_impar.append(num)
#
#     conf = input('Deseja continuar?: [S/N]').strip().upper()[0]
#     if conf in 'N':
#         break
#
# print(f'Lista dos números: {valores}')
# print(f'Números pares {num_par}')
# print(f'Número ímpar {num_impar}')


#Opção02
valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))

    resp = input('Deseja continuar? [S/N]').strip().upper()[0]
    if resp in 'N':
        break

for c, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista completa: {valores}')
print(f'A lista dos números pares: {pares}')
print(f'A lista dos números ímpares: {impares}')