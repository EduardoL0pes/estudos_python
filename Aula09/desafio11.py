somaidade = 0
mediaidade = 0
maioridadehomem = 0
homemvelho = ''
totmulher20 = 0
for c in range(4):
    print(f'----- {c + 1}ª PESSOA -----')
    nome = input('Qual seu nome? ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if c == 0 and sexo in 'Mn': #Verifica se ao colocar o Sexo foi em letra Minuscula ou maiuscula
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade:.0f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {homemvelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')