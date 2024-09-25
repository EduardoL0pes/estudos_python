car = float(input('Digite a velocidade: '))
if car >= 80:
    multa = (car - 80) * 7
    print('Sua velcoidade esta acima do permitido, MULTADO! \n Valor a pagar R${:.2f}'.format(multa))
else:
    print('Tudo ok, Faça uma boa Viagem!')