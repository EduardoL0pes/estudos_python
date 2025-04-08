from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(0,7):
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    calc = ano - ano_nascimento
    if calc >= 18:
        maior += 1
    else:
        menor += 1
if maior == 1:
    print(f'\033[1:35m{maior}\033[m pessoa é maior de idade e \033[1:35m{menor}\033[m pessoas são menores de idade.')
elif menor == 1:
    print(f'\033[1:35m{maior}\033[m pessoas são maiores de idade e \033[1:35m{menor}\033[m pessoa é menor de idade.')
else:
    print(f'\033[1:35m{maior}\033[m pessoas são maiores de idade e \033[1:35m{menor}\033[m pessoas são menores de idade.')