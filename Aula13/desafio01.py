valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))

print(f'Você digitou os valores {valores}')

maior = max(valores)
posicao_maior = []
for i, v in enumerate(valores):
    if v == maior:
        posicao_maior.append(i)
print(f'O maior valor digitado foi {maior} nas posições {posicao_maior}')

menor = min(valores)
posicao_menor = []
for i, v in enumerate(valores):
    if v == menor:
        posicao_menor.append(i)
print(f'O menor valor digitado foi {menor} nas posições {posicao_menor}')

# valor_num = []
# maior = menor = 0
# for c in range(0,5):
#     valor_num.append(int(input(f'Digite um valor para posição {c}: ')))
#
#     if c == 0:
#         maior = menor = valor_num[c]
#     else:
#         if valor_num[c] > maior:
#             maior = valor_num[c]
#         if valor_num[c] < menor:
#             menor = valor_num[c]
#
# print('-='*30)
# print(f'Você digitou os valores {valor_num}')
# print(f'O maior valor digitado foi {maior} nas posições ', end='')
# for i, v in enumerate(valor_num):
#     if v == maior:
#         print(f'{i}..', end='')
# print()
# print(f'O menor valor digitado foi {menor} nas posições ', end='')
# for i, v in enumerate(valor_num):
#     if v == menor:
#         print(f'{i}..', end='')
# print()
