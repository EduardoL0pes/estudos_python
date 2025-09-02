#Opção1
parada = soma = numeros = 0
while parada != 999:
    parada = int(input('Digite um valor: '))
    if parada != 999:
        soma += parada
        numeros += 1
print(f'Você digitou {numeros} números e a soma entre eles foi {soma}')