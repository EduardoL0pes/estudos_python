from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
calc = date.today().year - ano
print('O atleta tem {} anos.'.format(calc))
if calc <= 9:
    print('Você está na categoria MIRIM.')
elif calc <= 14:
    print('Você está na categoria INFANTIL.')
elif calc <= 19:
    print('Você está na categoria JUNIOR.')
elif calc <= 25:
    print('Você está na categoria SÊNIOR.')
else:
    print('Você está na categoria MASTER.')