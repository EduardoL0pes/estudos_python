from time import sleep
print('{:-^40}'.format('Caixa Eletrônico'))
saldo = 0
tentativas = 0
while True:
    print('\n' + '='*40)
    print('OPÇÕES:\n'
          '1 - Saldo\n'
          '2 - Saque\n'
          '3 - Depositar\n'
          '4 - Sair')
    opcao = int(input('Digite sua opção: '))
    sleep(0.5)
    print()
    if opcao == 1:
        print(f'Seu saldo é de R${saldo:.2f}')
    elif opcao == 2:
        print('OPÇÃO: Saque')
        saque = int(input('Qual valor deseja sacar? '))
        if saque <= saldo:
            saldo -= saque
            print('Saque realizado com SUCESSO!!\n'
                  f'valor sacado R${saque:.2f}\n'
                  f'Saldo restante R${saldo:.2f}')
        elif saque > saldo:
            print(f'Você não possui Saldo suficiente. Saldo R${saldo:.2f}')
    elif opcao == 3:
        deposito = int(input('Qual valor para deposito? '))
        if deposito <= 0:
            print('Valor inválido! Deposito deve ser positivo.\n')
        else:
            saldo += deposito
            print(f'Valor depositado com SUCESSO!!! Saldo atual R${saldo:.2f}')
    elif opcao == 4:
        print('Programa Finalizado. Volte Sempre!')
        break
    else:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE...')
        tentativas += 1
        if tentativas >= 3:
            print('Programa finalizado por excesso de tentativas inválidas.')
            break