valoratual = float(input('Quanto dinheiro você tem na carteira? R$'))
conversor = valoratual / 5.58
print('Você tem R${:.2f} e pode comprar US${:.2f} '.format(valoratual, conversor))
