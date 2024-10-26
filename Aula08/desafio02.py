num  = int(input('Digite um valor: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual á {}'.format(num, bin(num)[2:])) #[2:] para omitir o prefixo 0b
elif opcao == 2:
    print('{} convertido para OCTAL é igual á {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual á {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')