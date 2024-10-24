valor = float(input('Digite o valor a ser pago: R$'))
print('-==-='*10)
print('Opções de pagamento:'
          '\n á vista dinheiro/cheque: 10% de desconto, Digite 1'
          '\n á vista no cartão: 5% de desconto, Digite 2'
          '\n até 2x no cartão: sem desconto, Digite 3'
          '\n parcelas 3x ou mais no cartão: 20% de juros, Digite 4')
print('-==-='*10)
pagamento = int(input('Escolha a forma de pagamento: '))
if pagamento == 1:
    print('Opção de pagamento selecionado: dinheiro/cheque, aplicando desconto de 10%.')
    preco = valor * 10 / 100
    desconto = valor - preco
    print('Valor pago R${:.2f}'.format(desconto))
elif pagamento == 2:
    print('Opção de pagamento selecionado: á vista cartão, aplicando desconto de 5%.')
    preco = valor * 5 / 100
    desconto = valor - preco
    print('Valor pago R${:.2f}'.format(desconto))
elif pagamento == 3:
    print('Opção de pagamento selecionado: 2x no cartão, sem alteração no valor.')
    print('Valor pago R${:.2f}'.format(valor))
elif pagamento == 4:
    print('Opção de pagamento selecionado: parcelamento de 3x ou mais no cartão, aplicando juros de 20%.')
    preco = valor * 20 / 100
    juros = valor + preco
    print('Valor pago R${:.2f}'.format(juros))
