dados = dict()
dados['nome'] = input('Nome: ').title()
dados['media'] = float(input(f'Média de {dados['nome']}: '))
print()
for k, v in dados.items():
    print(f'{k} é igual a {v}')
if dados['media'] < 5:
    print('Situação REPROVADO.')
else:
    print('Situação APROVADO.')