# #Opção01
# dado = list()
# pessoas = list()
#
# while True:
#     dado.append(input('Digite seu nome: ').strip().title())
#     dado.append(float(input('Peso: ')))
#
#     pessoas.append(dado[:])
#     dado.clear()
#
#     resp = input('Deseja continuar? [S/N]').strip().upper()[0]
#     if resp == 'N':
#         break
#
# max_peso = pessoas[0][1]
# min_peso = pessoas[0][1]
#
# for p in pessoas:
#     if p[1] > max_peso:
#         max_peso = p[1]
#     if p[1] < min_peso:
#         min_peso = p[1]
#
# nomes_max = []
# nomes_min = []
#
# for p in pessoas:
#     if p[1] == max_peso:
#         nomes_max.append(p[0])
#     if p[1] == min_peso:
#         nomes_min.append(p[0])
#
# print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
# print(f'O maior peso foi de {max_peso}Kg. Peso de {nomes_max}.')
# print(f'O menor peso foi de {min_peso}Kg. Peso de {nomes_min}.')


#Opção02
