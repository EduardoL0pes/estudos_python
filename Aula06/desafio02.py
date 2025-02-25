velocidade = float(input('velocidade: '))
if velocidade > 80:
    maior = (velocidade - 80) * 9 #Multa por exceder o limite de velocidade
    print('Sua velocidade esta acima do permitido, MULTADO! \n Valor a pagar R${:.2f}'.format(maior))
elif velocidade < 30:
    menor = (30 - velocidade) * 8 #Multa por está abaixo da velocidade
    print('Sua velocidade está abaixo do permitido, MULTADO! \n Valor a pagar R${:.2f}'.format(menor))
else:
    print('Tudo ok, Faça uma boa Viagem!')
