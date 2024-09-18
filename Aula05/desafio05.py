frase = input('Digite uma frase: ').lower()
tamanho = len(frase)
e = frase.count('e', 0, tamanho)
first = frase.find('e')
last = frase.rfind('e')
print("""A frase que você digitou: {}
Quantidade de letras 'e' é: {}
Primeira letra 'e' fica na posição: {} 
Ultima letra 'e' fica na posição: {}""".format(frase, e, first, last))