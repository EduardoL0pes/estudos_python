nome = input('Digite seu nome completo: ')
div = nome.split()
first = nome[0]
last = nome[-1]
print("""Seu nome é: {}
Primeiro: {}
Ultimo: {} """.format(nome, first, last))