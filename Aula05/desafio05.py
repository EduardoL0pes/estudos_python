frase = input('Digite uma frase: ').strip().lower()
e = frase.count('e')
first = frase.find('e')
last = frase.rfind('e')
print("""
Quantidade de letras 'e' é: {}
Primeira letra 'e' fica na posição: {} 
Ultima letra 'e' fica na posição: {}""".format(e, first, last))