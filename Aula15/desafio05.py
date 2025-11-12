pessoas = {}
pessoas_lista = []
tot = 0

while True:
    pessoas['nome'] = input('Nome: ').title()
    pessoas['idade'] = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    if sexo in 'MF':
        pessoas['sexo'] = sexo
    elif sexo not in 'MF':
        while sexo not in 'MF':
            print('ERRO, somente M ou F. Tente novamente...')
            sexo = input('Sexo [M/F]: ').upper()
    tot += pessoas['idade']

    print('Dados cadastrados com SUCESSO!')
    pessoas_lista.append(pessoas.copy())

    resp = input('Deseja continuar? [S/N]: ').upper()
    if resp not in 'SN':
        while resp not in 'SN':
            print('ERRO, somente S ou N.')
            resp = input('Deseja continuar? [S/N]: ').upper()
    if resp in 'N':
        break
media = tot / len(pessoas_lista)

print('-='*30)
print(f'Ao todo foram cadastradas {len(pessoas_lista)} pessoas.')
print(f'A média de idade das pessoas cadastradas é igual a {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for m in pessoas_lista:
    if m['sexo'] == 'F':
        print(f'{m['nome']} ', end='')
print()
print('Lista de pessoas que estão acima da média: ')
for p in pessoas_lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()