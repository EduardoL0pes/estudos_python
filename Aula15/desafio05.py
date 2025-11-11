dic = dict()
lista = list()
tot = 0
soma_idade = 0
media = 0
mulheres = list()

while True:
    dic['nome'] = input('Nome: ').title()
    dic['sexo'] = input('Sexo [M/F]: ').upper()
    dic['idade'] = int(input('Idade: '))
    tot += 1
    soma_idade += dic['idade']
    media = soma_idade / tot

    lista.append(dic.copy())

    if dic['sexo'] == 'F':
        mulheres.append(dic['nome'])

    resp = input('Deseja continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break

print('-'*30)
print(f'Foram cadastradas {tot} pessoas.')
print(f'A média de idade do grupo é de {media} anos.')
print(f'As mulheres cadastradas foram {mulheres}.')
