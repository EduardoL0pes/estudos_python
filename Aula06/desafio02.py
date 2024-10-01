car = float(input('Digite a velocidade: '))
if car > 80:
    maior = (car - 80) * 9 #Multa de 9reais por km acima do limite
    print('Sua velocidade esta acima do permitido, MULTADO! \n Valor a pagar R${:.2f}'.format(maior))
elif car < 30:
    menor = (30 - car) * 8
    print('Sua velocidade está abaixo do permitido, MULTADO! \n Valor a pagar R${:.2f}'.format(menor))
else:
    print('Tudo ok, Faça uma boa Viagem!')