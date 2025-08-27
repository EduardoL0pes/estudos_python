#Opção 1
"""sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ')
print(f'Sexo {sexo} registrado com sucesso')"""

#Opção 2
nome = input('Digite seu nome: ').strip().title()
idade = int(input('Digite sua idade: '))
sexo = ''
sexoesp = ''
while sexo == '':
    sexo = input('Informe seu sexo: [M/F] ').strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Dados coletados com sucesso!')
        if sexo == 'M':
            sexoesp += 'Maculino'
        else:
            sexoesp += 'Feminino'
    while sexo != 'M' and sexo != 'F':
        print('Sexo informado está incorreto!')
        sexo = input('Informe o sexo novamente: [M/F] ').strip().title()
        if sexo == 'M' or sexo == 'F':
            print('Dados coletados com sucesso!')
            if sexo == 'M':
                sexoesp += 'Masculino'
            else:
                sexoesp += 'Feminino'
print(f'Seu nome é {nome} você tem {idade} anos e é do sexo {sexoesp}.')