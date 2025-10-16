# nomes = list()
# nomes.append('José')
# nomes.append(60)
# print(f'variavel nomes: {nomes}')
#
# pessoas = list()
# pessoas.append(nomes[:])
# nomes[0] = 'Maria'
# nomes[1] = 65
# pessoas.append(nomes[:])
# print(pessoas)

#galera = [['José', 50], ['Maria', 45], ['Joaquim', 65], ['Ana', 35]]
# print(galera[0])     #Acessa a lista que esta na posição 0. resultado: ['José', 50]
# print(galera[0][0])  #Imprime somente o dado da posição 0 da primeira e segunda lista. resultado: José
# print(galera[0][1])  #Imprime somente o dado da posição 0 da primeira lista e acessa o dado na posição 1 da segunda lista. resultado: 50
# print(galera[2][0])  #resultado: Joaquim

#for p in galera:
    #print(p[0]) #Imprime somente os nomes
    #print(p[1]) #Imprime somente as idades
    #print(f'{p[0]} tem {p[1]} anos de idade.')   #Imprime nome de cada um da lista e suas respectivas idades

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')