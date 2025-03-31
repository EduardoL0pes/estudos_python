soma = 0
for c in range(1, 6+1):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os valores pares é igual a {soma}')