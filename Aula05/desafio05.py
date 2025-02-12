#Forma 1
frase = input('Digite uma frase: ').strip().lower()
e = frase.count('e')
first = frase.find('e')
last = frase.rfind('e')
print("""
Quantidade de letras 'e' é: {}
Primeira letra 'e' fica na posição: {} 
Ultima letra 'e' fica na posição: {}""".format(e, first, last))

#Forma 2
"""frase = input('Digite uma frase qualquer: ').strip().lower()
print('Qt. letras "A" na frase: ', frase.count('a'))
print('Aparece a primeira vez na posição: ', frase.find('a'))
print('Aparece pela última vez na posição: ', frase.rfind('a'))"""
