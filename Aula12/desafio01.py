#Opção01
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
               'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze',
               'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = 0
for c in range(num, len(num_extenso)):
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Número informado não existe, tente novamente.')
    else:
        print(f'O número que você digitou é {num_extenso[num]}')
        break

#Opção02
# cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
#         'seis', 'sete', 'oito', 'nove', 'dez',
#         'onze', 'doze', 'treze', 'quatorze', 'quinze',
#         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
#
# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         print(f'Você digitou o número {cont[num]}')
#         break
#     else:
#         print('Tente novamente.', end='')