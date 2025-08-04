num1 = ''
num2 = ''
while num1 == '' and num2 == '':
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    print("""\033[1;33mAbaixo algumas Opções:
    [1]Somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    \033[m""")
    res = int(input('Escolha alguma das opções acima: '))
    #sleep
    if res == 1:
        print('Opção escolhida [SOMAR]')
        soma = num1 + num2
        print(f'A soma de \033[1;32m{num1} + {num2} é {soma}\033[m')
    if res == 2:
        print('Opção escolhida [MULTIPLICAR]')
        mult = num1 * num2
        print(f'A multiplicação de \033[1;32m{num1} x {num2} é {mult}\033[m')
    if res == 3:
        print('Opção escolhida [MAIOR]')
        #sleep
        if num1 > num2:
            print(f'O número {num1} é maior.')
        else:
            print(f'O número {num2} é maior.')
    if res == 4:
        print('Opção escolhida [NOVOS NÚMEROS]')
        confirmacao = input('Você realmente deseja escolher novos números? [S/N] ').upper()
        if confirmacao == 'S':
            while confirmacao == 'S':
                novo_num1 = int(input('Digite um novo valor: '))
                novo_num2 = int(input('Digite outro novo valor: '))
                print(f'Os números escolhidos foram \033[1;32m{novo_num1} e {novo_num2}\033[m')
                break
        if confirmacao == 'N':
            print('Números sem alteração.')
        if confirmacao != 'S' or confirmacao != 'N':
            print('Opção inválida, tente novamente!')
            while confirmacao != 'S' and confirmacao != 'N':
                novo_num1 = int(input('Digite um novo valor: '))
                novo_num2 = int(input('Digite outro novo valor: '))
                print(f'Os números escolhidos foram \033[1;32m{novo_num1} e {novo_num2}\033[m')
                break
                #erro
    if res == 5:
        print('Finalizando programa... Obrigado e tenha um bom dia!')
print('fim')