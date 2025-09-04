# tab = int(input('Digite um número para ver a sua TABUADA: '))
# num = 0
# while True:
#     num += 1
#     if num == 11:
#          break
#     print(f'{tab}x{num} = {num*tab}')


# tab = int(input('Digite um número para mostrar sua TABUADA: '))
# num = 0
# while num < 10:
#     num += 1
#     print(f'{tab}x{num} = {num * tab}')


while True:
    tab = int(input('Quer ver a TABUADA de qual valor? '))
    print('-' * 30)
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab*c}')
    print('-' * 30)
print('Finalizando o Programa...')