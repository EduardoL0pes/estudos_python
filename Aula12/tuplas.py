# #As tuplas são IMUTÁVEIS

# lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
# print(lanche) #resultado: 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
# print(lanche[-1]) #res: Pudim
# print(lanche[:-2]) #res: Hamburguer, Pizza
# print(lanche[-3:]) #res: Suco, Pizza, Pudim
# print(lanche[1:3]) #res: suco, pizza   obs:desconsidera o ultimo elemento 'Pudim'
# print(lanche[:2]) #res: Hamburguer, Suco
# print(lanche[2:]) #res: Pizza, Pudim
# print(sorted(lanche)) #res: vai ordenar os lanches para hamburguer, pizza, pudim, suco tbm transformará a tupla em uma lista

#lanche = 'Hamburguer', 'Suco', 'Pizza', 'Batata Frita', 'Pudim'
# for c in range(0, len(lanche)):
#     print(f'{lanche[c]} na posição {c}')

# for pos, c in enumerate(lanche):
#     print(f'{c} na posição {pos}')

a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c) #res: 5,8,1,2,2,5,4
print(c.index(5)) #res: posição 0
print(c.index(5, 1)) #res: valor procurado é 5 que esta na posição 5