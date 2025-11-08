from datetime import date

dados = {
    'nome': input('Nome:').title(),
    'idade': int(input('Ano de Nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 não tem): '))
}
dados['idade'] = date.today().year - dados['idade']

if dados['ctps'] == 0:
    print('=' * 30)
    for keys, valores in dados.items():
        print(f'{keys} tem o valor {valores}')

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = (35 - (date.today().year - dados['contratação'])) + dados['idade']
    print('=' * 30)

    for k, v in dados.items():
        print(f'{k} tem o valor {v}')