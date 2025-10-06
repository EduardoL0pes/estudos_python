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