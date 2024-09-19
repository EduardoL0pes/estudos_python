nome = input('Digite seu nome completo: ')
div = nome.split()
first = div[0]
last = div[-1]
print("""Seu nome é: {}
Primeiro: {}
Ultimo: {} """.format(nome, first, last))