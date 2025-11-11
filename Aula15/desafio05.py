dic = dict()
lista = list()
tot = 0
soma_idade = 0

while True:
    dic['nome'] = input('Nome: ').title()
    dic['sexo'] = input('Sexo [M/F]: ').upper()
    dic['idade'] = int(input('Idade: '))
    tot += 1
    soma_idade += dic['idade']

    lista.append(dic.copy())

    resp = input('Deseja continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break

print('-'*30)
print(f'Foram cadastradas {tot} pessoas.')
print(f'A média de idade do grupo é de {soma_idade / tot} anos.')

for i in lista:
    for v in i.values():
        if v == 'F':
            print(dic['nome'])
