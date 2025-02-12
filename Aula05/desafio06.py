#Forma 1
nome = input('Digite seu nome completo: ').strip()
div = nome.split()
first = div[0]
last = div[-1]
print("""Seu nome é: {}
Primeiro: {}
Ultimo: {} """.format(nome, first, last))

#Forma 2
"""nome = input('Digite seu nome completo: ').split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')"""
