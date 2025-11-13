galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').title()

    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite somente M ou F.')
    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = input('Deseja continuar? [S/N]: ').upper()
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
media = soma / len(galera)

print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(p['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('-='*30)
print('<< ENCERRADO >>')