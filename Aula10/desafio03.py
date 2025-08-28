#Opção1
# num1 = ''
# num2 = ''
# while num1 == '' and num2 == '':
#     num1 = int(input('Digite um valor: '))
#     num2 = int(input('Digite outro valor: '))
#     print("""\033[1;33mAbaixo algumas Opções:
#     [1]Somar
#     [2]multiplicar
#     [3]maior
#     [4]novos números
#     [5]sair do programa
#     \033[m""")
#     res = int(input('Escolha alguma das opções acima: '))
#     if res == 1:
#         print('Opção escolhida [SOMAR]')
#         soma = num1 + num2
#         print(f'A soma de \033[1;32m{num1} + {num2} é {soma}\033[m')
#     if res == 2:
#         print('Opção escolhida [MULTIPLICAR]')
#         mult = num1 * num2
#         print(f'A multiplicação de \033[1;32m{num1} x {num2} é {mult}\033[m')
#     if res == 3:
#         print('Opção escolhida [MAIOR]')
#         if num1 > num2:
#             print(f'O número {num1} é maior.')
#         else:
#             print(f'O número {num2} é maior.')
#     if res == 4:
#         print('Opção escolhida [NOVOS NÚMEROS]')
#         confirmacao = input('\033[1;33mVocê realmente deseja escolher novos números? [S/N]\033[m ').upper()
#         if confirmacao == 'S':
#             while confirmacao == 'S':
#                 novo_num1 = int(input('Digite um novo valor: '))
#                 novo_num2 = int(input('Digite outro novo valor: '))
#                 print(f'Os números foram atualizados \033[1;32m{novo_num1}\033[m e \033[1;32m{novo_num2}\033[m')
#                 break
#         if confirmacao == 'N':
#             print('Números sem alteração.')
#     if res == 5:
#         print('Finalizando programa... Obrigado e tenha um bom dia!')
# print('fim')

from time import sleep

#Opção2
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('-=-=' * 10)
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa
    ''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é igual á {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é igual á {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('Valores atualizados')
    elif opcao == 5:
        print('Finalizando programa...')
        sleep(1)
print('Programa finalizado, volte sempre!')