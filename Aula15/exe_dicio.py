pessoas = {'nome': 'Eduardo', 'idade': 29, 'sexo': 'M'}
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
print()

# for k in pessoas.keys():
#     print(k)
# saída: nome, idade, sexo (um abaixo do outro)

# for v in pessoas.values():
#     print(v)
# saída: Eduardo, 29, M (um abaixo do outro)

for k, v in pessoas.items():
    print(f'{k} = {v}')
# saída: nome = Eduardo, idade = 29,  sexo = M (um abaixo do outro)
print()

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
#print(brasil[1]['uf'])    # Saída: São Paulo
#print(brasil[0]['sigla']) #Saída: RJ

estado = {}
brazil = []
for c in range(0, 2):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ').upper()
    brazil.append(estado.copy())
for e in brazil:
    for v in e.values():
        print(v, end='')
    print()