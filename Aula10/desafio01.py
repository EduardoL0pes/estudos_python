"""sexo = ''
while sexo == '':
    sexo = input('Informe seu sexo: [M/F] ').upper()
    if sexo == 'M':
        print('Dados coletados com sucesso!')
    if sexo != 'M':
        print('Sexo informado está incorreto! Tente novamente.')
        sexo = input('Informa o sexo novamente: ')
print('fim')"""

sexo = ''
while sexo == '':
    sexo = input('Informe seu sexo: [M/F] ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo informado está incorreto!')
        sexo = input('Informe o sexo novamente: [M/F] ').upper()
        while sexo != 'M' and sexo != 'F':
            sexo = input('Informe o sexo novamente: [M/F] ').upper()
            if sexo == 'M' and sexo != 'F':
                print('Dados coletados com sucesso!')
    else:
        print('Dados coletados com sucesso!')
print('fim')

"""identificar erro line 15, apos imprimir primeiro erro de sexo, retorna 'fim' em sequência"""