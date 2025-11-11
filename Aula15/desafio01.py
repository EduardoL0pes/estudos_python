dados = dict()
dados['nome'] = input('Nome: ').title()
dados['media'] = float(input(f'Média de {dados['nome']}: '))

if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('-='*30)

for k, v in dados.items():
    print(f'  -{k} é igual a {v}')


# dados = dict()
# dados['nome'] = input('Nome: ').title()
# dados['media'] = float(input(f'Média de {dados['nome']}: '))
# print('-'*30)
# for k, v in dados.items():
#     print(f'{k} é igual a {v}')
# if dados['media'] < 5:
#     print('Situação REPROVADO.')
# elif dados['media'] < 7:
#     print('RECUPERAÇÃO.')
# else:
#     print('APROVADO')