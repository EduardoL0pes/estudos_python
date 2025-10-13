# valores = []
# cont = 0
# while True:
#     num = int(input('Digite um valor: '))
#     valores.append(num)
#     cont += 1
#
#     conf = ' '
#     while conf not in 'SN':
#         conf = input('Deseja continuar? [S/N]').strip().upper()[0]
#     if conf == 'N':
#         break
#
# print()
#
# print(f'Lista original: {valores}')
# print(f'Foi digitou {cont} elementos.')
# print(f'Lista decrescente: {sorted(valores, reverse=True)}')
#
# if 5 in valores:
#     print(f'O valor 5 faz parte da lista! E esta na posição {valores.index(5)}.')
# else:
#     print('O valor 5 não faz parte da sua lista.')


#Opção02
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? [S/N]').strip().upper()[0]
    if resp in 'N':
        break

print('-='*30)
print(f'Você digitou {len(valores)} elementos')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print(f'O valor 5 faz parte da lista! E esta na posição {valores.index(5)}.')
else:
    print('O valor 5 não foi encontrado na lista!')