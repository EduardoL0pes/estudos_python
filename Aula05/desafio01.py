#Forma 1
nome = input('Digite seu nome completo: ').strip()
u = nome.upper()
l = nome.lower()
qt = len(nome) - nome.count(' ')
#qt = len(nome.replace(' ', '')) #uma forma de retirar os espaços entres as palavras
#pn = nome.find(' ') #uma forma de mostrar a quantidade de caracteres do primeiro nome
pn = nome.split()
print("""
Nome completo é: {}
Letras maiusculas: {}
Letras minusculas: {}
Quantidade de letras: {}
Qt de letras no primeiro nome: {}""" .format(nome, u, l, qt, len(pn[0])))

#Forma 2
nome = input('Digite seu nome completo: ').strip()
print(f"""
Nome completo: {nome}
Qt de caracteres: {len(nome)}
Letras Minúsculas: {nome.lower()}
Letras Maiúsculas: {nome.upper()}
Nome sem espaços:  {nome.replace(' ', '')}
Qt de caracteres primeiro nome: {len(nome.split()[0])}
""")
