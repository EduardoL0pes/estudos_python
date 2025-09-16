##Opção01
# maiores = masc = fem = 0
# sexo = ''
# while True:
#     while sexo != 'M' or sexo != 'F':
#         sexo = input('Digite o sexo: [M/F] ').upper().strip()
#         if sexo == 'M' or sexo == 'F':
#             idade = int(input('Digite a idade: '))
#             conf = input('Deseja continuar o cadastro? [S/N] ').upper().strip()
#             if conf == 'S':
#                 if idade >= 18:
#                     maiores += 1
#                 if sexo == 'M':
#                     masc += 1
#                 if sexo == 'F' and idade < 20:
#                     fem += 1
#             else:
#                 print('-='*30)
#                 print('CADASTRO REALIZADADO COM SUCESSO !')
#                 print('----FIM DO PROGRAMA----')
#                 print(f'Um total de {maiores} pessoas foram cadastradas com mais de 18 anos.')
#                 print(f'Foram cadastrados {masc} homens.')
#                 print(f'Foram {fem} mulheres cadastradas com menos de 20 anos.')
#                 break
#     break

##Opção02
tot18 = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de {homem} homens cadastrados.')
print(f'Total de {mulher} mulheres cadastradas com menos de 20 anos.')