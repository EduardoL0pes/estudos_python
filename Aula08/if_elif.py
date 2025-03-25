nome = input('Qual é seu nome? ')
if nome == 'Eduardo':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'João' or nome == 'José':
    print('Seu nome é muito popular no Brasil')
elif nome in 'Juliana Pedro Creuza':
    print('Seu nome é bem incomum')
else:
    print('Seu nome é bem normal')
print('Tenha uma boa tarde, {}!'.format(nome))
