#Opção I - Valores ímpares multiplos de 3
"""soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
print(soma)"""

#Opação II
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
    #cont += 1 #Todos os valores ímpares dentro da contagem entre 1 - 501
        cont += 1 #Todos os valores ímpares que são múltiplos de 3
print(f'A soma de todos os \033[1:35m{cont}\033[m valores solicitados é de \033[1:35m{soma}\033[m')