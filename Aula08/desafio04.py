from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
calc = date.today().year - ano
if calc <= 17:
    falta = 18 - calc
    print('Você tem atualmente {} anos, ainda não tem idade para se alistar, faltam {} anos'.format(calc, falta))
elif calc == 18:
    print('Você tem {} anos já é hora de se alistar'.format(calc))
elif calc >= 19:
    print('Você tem {} anos já passou do tempo de se alistar'.format(calc))
