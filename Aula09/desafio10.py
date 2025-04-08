maior_peso = 0
menor_peso = 0
for c in range(5):
    peso = float(input(f'Informe seu peso{c + 1} (em kg): '))
    if c == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso informado foi \033[1:35m{maior_peso}\033[mkg')
print(f'O menor peso informado foi \033[1:35m{menor_peso}\033[mkg')
