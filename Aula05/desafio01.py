nome = input('Digite seu nome completo: ')
u = nome.upper()
l = nome.lower()
qt = len(nome.replace(' ', ''))
pn = len(nome[0:6])
print("""
Nome completo é: {}
Letras maiusculas: {}
Letras minusculas: {}
Quantidade de letras: {}
Qt de letras no primeiro nome: {}""" .format(nome, u, l, qt, pn))