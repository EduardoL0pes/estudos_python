listagem = 'Pão', 1, 'Leite', 3.10, 'Mortadela', 3.50, 'Mussarela', 4.50
print('-'*30)
print('LISTAGEM DE PREÇO'.center(30))
print('-'*30)
print('{:.<20}R$ {:.2f}'.format(listagem[0], listagem[1]))
print('{:.<20}R$ {:.2f}'.format(listagem[2], listagem[3]))
print('{:.<20}R$ {:.2f}'.format(listagem[4], listagem[5]))
