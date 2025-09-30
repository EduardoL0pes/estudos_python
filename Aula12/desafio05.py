#Opção01
# listagem = 'Pão', 1, 'Leite', 3.10, 'Mortadela', 3.50, 'Mussarela', 4.50
# print('-'*30)
# print('LISTAGEM DE PREÇO'.center(30))
# print('-'*30)
# print('{:.<20}R$ {:.2f}'.format(listagem[0], listagem[1]))
# print('{:.<20}R$ {:.2f}'.format(listagem[2], listagem[3]))
# print('{:.<20}R$ {:.2f}'.format(listagem[4], listagem[5]))
# print('{:.<20}R$ {:.2f}'.format(listagem[6], listagem[7]))

#Opção02
listagem = ('Pão', 1,
            'Leite', 3.10,
            'Mortadela', 3.50,
            'Mussarela', 4.50,
            'Presunto', 6.50,
            'Pão de queijo', 8.10)
print('-'*30)
print('LISTAGEM DE PREÇOS'.center(30))
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<23}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
