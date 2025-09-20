nome = input('Digite uma palavra: ').strip().upper()
contador = 0
while nome in 'AEIOU':
    contador += 1
print(f'A palavra {nome} tem {contador} vogais.')
