# #Opção01
num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))
num_tup = (num, num2, num3, num4)

print(f'Você digitou os valores {num_tup}')
if num_tup.count(9):
    print(f'O valor 9 foi digitado {num_tup.count(9)} vezes.')
else:
    print(f'O valor 9 foi digitado 0 vezes.')
if 3 in num_tup:
    print(f'O valor 3 está na posição {num_tup.index(3)+1}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print(f'Números pares são: ', end='')
for c in num_tup:
    if c % 2 == 0:
        print(c, end=' ')


#Opção02
# num = (int(input('Digite o primeiro valor: ')),
#        int(input('Digite o segundo valor: ')),
#        int(input('Digite o terceiro valor: ')),
#        int(input('Digite o quarto valor: ')))
# print(f'Você digitou os valores: {num}')
# print(f'O número 9 apareceu {num.count(9)} vezes.')
# if 3 in num:
#     print(f'O número 3 está na posição {num.index(3)+1}ª')
# else:
#     print('O número 3 não foi encontrado em nenhuma posição.')
# print('Os numeros pares são: ', end='')
# for c in num:
#     if c % 2 == 0:
#         print(c, end=' ')