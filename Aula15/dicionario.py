#dados = {} ou dict()
dados = {'nome': 'Eduardo', 'idade': 29}
print(dados['nome'])
print(f'{dados['idade']} \n')

#Para adicionar um novo elemento ao dicionario.
print('-adiciona novo elemento-')
dados['sexo'] = 'M'
print(f'{dados} \n') #saída: {'nome': 'Eduardo', 'idade': 29, 'sexo': 'M'}

#remover um elemento.
print('-remove um elemento-')
del dados['idade']
print(f'{dados} \n')  #saída: {'nome': 'Eduardo', 'sexo': 'M'}

filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}
print(filme)
print(filme.values()) #saída: 'Star Wars', 1977, 'George Lucas'
print(filme.keys())   #saída: 'titulo', 'ano', 'diretor'
print(filme.items())  #saída: 'titulo', 'Star Wars', 'ano', 1977, 'diretor', 'George Lucas'

print()

print('Aplicanco looping...')
for k, v in filme.items():  # 'k' é as keys e o 'v' é os values
    print(f'o {k} é {v}.')  #Saída: o titulo é Star Wars.
                            #       o ano é 1977.
                            #       o diretor é George Lucas.