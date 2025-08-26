numero = int(input('Digite um número: '))
fatorial = 1
if numero < 0:
    print('Não é possível calcular o fatorial de um número negativo.')
elif numero == 0:
    print('O fatorial de 0 é 1.')
else:
    while numero > 0:
        fatorial = fatorial * numero    #loop1 5, loop2 20, loop3 60, loop4 120, loop5 120.
        numero -= 1                     #decrementando
print(f'O fatorial é {fatorial}.')
