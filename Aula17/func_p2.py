# Interactive Help
# Docstrings
# Argumentos opcionais
# Escopo de variáveis
# Retorno de resultados


### função de ajuda

# help()
# print(input.__doc__)

# -------------------------------------

### Docstrings

# def contador (i,f,p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(c, end=' ')
#         c += p
#     print('FIM!')

# contador(2,10,2)
#help(contador)

# -----------------------------------

### Argumentos opções

#def somar(a=0,b=0,c=0)  #podendo tbm colocar =0 para todos os parametros e a função somar() 'vazia' não irá aparecer erro

# def somar(a,b,c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(3,2,5)
# somar(8,4)

# -----------------------------------

### Escopo de variáveis

#Escopo Local
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A local vale {a}') #8
    print(f'B local vale {b}') #9 soma A do escopo global com B do escopo local
    print(f'C local vale {c}') #2

#Escopo Global
a = 5
print(f'A global vale {a}')
teste(a)