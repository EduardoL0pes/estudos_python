from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
calc = date.today().year - ano

if calc <= 9:
    print('Você esta na categoria MIRIM, entre 1 á 9 anos')
elif 10 <= calc <= 14:
    print('Você esta na categoria INFANTIL, entre 10 á 14 anos')
elif 15 <= calc <= 19:
    print('Você esta na categoria JUNIOR, entre 15 á 19 anos')
elif calc == 20:
    print('Você esta na categoria SÊNIOR')
else:
    print('Você esta na categoria MASTER')