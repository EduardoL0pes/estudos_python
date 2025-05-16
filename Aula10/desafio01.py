nome = input('Digite seu nome: ').strip().title()
idade = int(input('Digite sua idade: '))
sexo = ''
sexoesp = ''
while sexo == '':
    sexo = input('Informe seu sexo: [M/F] ').upper()
    if sexo == 'M' or sexo == 'F':
        print('Dados coletados com sucesso!')
        if sexo == 'M':
            sexoesp += 'Maculino'
        else:
            sexoesp += 'Feminino'
    while sexo != 'M' and sexo != 'F':
        print('Sexo informado está incorreto!')
        sexo = input('Informe o sexo novamente: [M/F] ').upper()
        if sexo == 'M' or sexo == 'F':
            print('Dados coletados com sucesso!')
            if sexo == 'M':
                sexoesp += 'Masculino'
            else:
                sexoesp += 'Feminino'
print(f'Seu nome é {nome} você tem {idade} anos e é do sexo {sexoesp}.')