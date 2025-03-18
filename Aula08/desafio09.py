from time import sleep
produto = float(input('Valor do produto: R$'))
print("""\033[1;33mFormas de pagamento:
[1] á vista dinheiro/cheque: 10% desconto.
[2] á vista no cartão: 5% desconto.
[3] até 2x no cartão: sem juros.
[4] 3x ou mais no cartão: 20% de juros.
\033[m""")
pagamento = int(input('Digite a forma de pagamento: '))
print('\033[1;33mCARREGANDO...\033[m')
if pagamento == 1:
          print('\033[1;33m[1] á vista dinheiro/cheque.\033[m')
          desconto_produto = produto - (produto * 10 / 100)
          print(f'Valor a ser pago com 10% de desconto é de \033[0;32R${desconto_produto:.2f}\033[m')
elif pagamento == 2:
          print('\033[1;33m[2] á vista no cartão\033[m')
          cartao_desconto_produto = produto - (produto * 5 / 100)
          print(f'Valor a ser pago com 5% de desconto é de \033[0;32mR${cartao_desconto_produto:.2f}\033[m')
elif pagamento == 3:
          print('\033[1;33m[3] até 2x no cartão. Valor sem alteração.\033[m')
          parcela_produto = produto / 2
          print(f'Parcelado em 2x de \033[0;32mR${parcela_produto:.2f}\033[m')
elif pagamento == 4:
          print('\033[1;33[4] 3x ou mias no cartão.')
          qt_parcela = int(input('Quantas vezes? '))
          if qt_parcela >= 3:
                    juros_produto = produto + (produto * 20 / 100)
                    calc_parcelas = juros_produto / qt_parcela
                    print(f'Valor das parcelas é de \033[0;32mR${calc_parcelas:.2f}\033[m \nValor Total: \033[0;32mR${juros_produto:.2f}\033[m')
          else:
                    print('\033[1;31mOpção Inválida! Somante para parcelamentos acima de 3x.\033[m')
else:
          print('\033[1;31mOpção Inválida! Tente novamente.\033[m')
                              


#Opção1
"""print('{:=^40}'.format(' SIMULDOR DE COMPRAS '))
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
    print('Opção selecionada está inválida. Tente novamente!')"""
