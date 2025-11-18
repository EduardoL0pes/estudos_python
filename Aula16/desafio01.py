def area(larg, comp):
    a = larg * comp
    print(f'A área de um terrono {larg}x{comp} é de {a}m².')

print('Controle de Terrenos'.center(30))
print('-'*30)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)


# def area(l, c):
#     tot = l * c
#     print(f'A área de um terreno {l}x{c} é de {tot}m².')
#
# print('Controle de Terrenos'.center(30))
# print('-'*30)
# area(float(input('Largura (m): ')),float(input('Comrpimento (m): ')))
