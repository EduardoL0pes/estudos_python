valores = []
conf = 'S'
while conf == 'S':
    num = (int(input('Digite uma valor: ')))

    if num in valores:
        print('Esse número ja foi adicionado.')
    else:
        valores.append(num)
        print('Número adicionado com sucesso!')

    conf = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if conf == 'N':
        break
print(f'Você adicionou os valores {sorted(valores)}')
