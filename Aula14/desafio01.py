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


# Opção02
princ = []
temp = []
mai = men = 0
while True:
    temp.append(input('Digite seu nome: ').strip().title())
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp in 'N':
        break

print(f'Ao todo, você cadastrou {len(princ)} pessoas.')

print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
