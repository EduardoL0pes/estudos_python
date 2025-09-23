palavra = input('Digite uma palavra/frase: ').strip().lower()
remove_esp = palavra.replace(' ','')

i = 0
total_vogais = 0
total_cons = 0

while i < len(remove_esp):
    letra = remove_esp[i]
    if letra in 'aeiou':
        total_vogais += 1
    elif letra.isalpha():
        total_cons += 1
    i += 1
print(f'nome: {palavra} tem {total_vogais} vogais e {total_cons} consoantes.')

# #Usando loop for
# palavra = 'programador'
# vogais = 0
# for i in range(len(palavra)):
#     letra = palavra[i].lower()
#     if letra in 'aeiou':
#         vogais += 1
#     i += 1
# print(f'nome: {palavra} tem {vogais} vogais.')