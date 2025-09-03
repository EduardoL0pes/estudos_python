tab = int(input('Digite um número para ver a sua TABUADA: '))
num = 0
while True:
    num += 1
    if num == 11:
        break
    print(f'{tab}x{num} = {num*tab}')
