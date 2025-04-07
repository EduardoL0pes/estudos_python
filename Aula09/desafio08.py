texto = input('Escreva uma frase: ')
#Remove espaços e converte para minúsculas
texto_limpo = ''.join(c for c in texto if c.isalnum()).lower()
#verifica se o texto é igual ao seu reverso
if texto_limpo == texto_limpo[:: -1]:
    print(f'A frase \033[1:32m{texto}\033[m é um palíndromo.')
else:
    print('Não é um palíndromo.')