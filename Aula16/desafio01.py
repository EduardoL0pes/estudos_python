print('Controle de Terrenos'.center(30))
print('-'*30)

def area(l, c):
    tot = l * c
    print(f'A área de um terreno {l}x{c} é de {tot}m².')

area(float(input('Largura (m): ')),float(input('Comrpimento (m): ')))
