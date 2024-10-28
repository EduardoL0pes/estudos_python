print('{:=^40}'.format(' SIMULDOR DE COMPRAS '))
valor = float(input('Digite o valor a ser pago: R$'))
print('-==-='*10)
print('Opções de pagamento:'
          '\n [ 1 ] á vista dinheiro/cheque: 10% de desconto'
          '\n [ 2 ] á vista no cartão: 5% de desconto'
          '\n [ 3 ] até 2x no cartão: sem desconto'
          '\n [ 4 ] parcelas 3x ou mais no cartão: 20% de juros')
print('-==-='*10)
pagamento = int(input('Escolha a forma de pagamento: '))
if pagamento == 1:
    print('Opção de pagamento selecionado: dinheiro/cheque, aplicando desconto de 10%.')
    preco = valor - ( valor * 10 / 100)
    print('Valor final á ser pago R${:.2f}'.format(preco))
elif pagamento == 2:
    print('Opção de pagamento selecionado: á vista cartão, aplicando desconto de 5%.')
    preco = valor - (valor * 5 / 100)
    print('Valor final á ser pago R${:.2f}'.format(preco))
elif pagamento == 3:
    print('Opção de pagamento selecionado: 2x no cartão SEM JUROS.')
    divisao = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f}, Valor total a ser pago será de R${:.2f}'.format(divisao, valor))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas?: '))
    print('Opção de pagamento selecionado: parcelamento de 3x ou mais no cartão, aplicando juros de 20%.')
    preco = valor + ( valor * 20 / 100)
    divisao = preco / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f}, Valor total a ser pago será de R${:.2f}'.format(parcelas, divisao, preco))
else:
    print('Opção selecionada está inválida. Tente novamente!')
