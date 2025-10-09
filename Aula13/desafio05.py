valores = []
num_par = []
num_impar = []
while True:
    for c in range(0, 3):
        num = int(input('Digite um valor: '))
        valores.append(num)

        if num % 2 == 0:
            num_par.append(num)
        else:
            num_impar.append(num)

    conf = ' '
    while conf not in 'SN':
        conf = input('Deseja continuar?: [S/N]').strip().upper()[0]
    if conf == 'N':
        break

print(f'Lista dos números: {valores}')
print(f'Números pares {num_par}')
print(f'Número ímpar {num_impar}')
