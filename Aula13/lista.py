#num = [2, 9, 5, 1]
#num[2] = 3     ## valor que esta na posição [2] vai ser substituido pelo valor 3
#num.append(7)  ## acrestenta o numero 7 ao final da lista
#num.sort()     ## ordena os numeros para crescente
#num.sort(reverse=True)  ## ordena os numeros para decrescente
#num.insert(2,0)  ## adiciona o numero 0 na posição 2
#num.pop()        ## remove o ultimo elemento da lista
#num.pop(2)       ## remove o elemento na posição 2
#num.remove(2)    ##remove o numero 2 e se houver mais de um numero 2 na lista ele removerá sempre o primeiro a aparecer
#print(num)


##le um input de 3 valores armazena na variavel valores, depois percorre cada valor mostrando sua posição
# valores = list()
# for cont in range(0, 3):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')

a = [2, 3, 4, 7]
#b = a   ##interliga a lista, ou seja as alterações que eu fizer tbm irá alterar a variavel original
b = a[:] ##faz uma copia da lista, podendo alterar os elementos sem modificar a variavel original
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')