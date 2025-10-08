valores = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    cont += 1

    conf = ' '
    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N]').strip().upper()[0]
    if conf == 'N':
        break

print()

print(f'Lista original: {valores}')
print(f'Foi digitou {cont} elementos.')
print(f'Lista decrescente: {sorted(valores, reverse=True)}')

if 5 in valores:
    print(f'O valor 5 faz parte da lista! E esta na posição {valores.index(5)}.')
else:
    print('O valor 5 não faz parte da sua lista.')