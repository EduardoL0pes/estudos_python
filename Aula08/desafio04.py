from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
print('''Informe seu gênero: 
[ 1 ] Maculino
[ 2 ] Feminino''')
sexo = int(input('Qual seu gênero?: '))
calc = date.today().year - ano
if calc <= 17 and sexo == 1:
    falta = ano + 18
    print('Você tem atualmente {} anos, ainda não tem idade para se alistar, você deverá se alistar em {}.'.format(calc, falta))
elif calc == 18 and sexo == 1:
    print('Você tem {} anos já é hora de se alistar.'.format(calc))
elif calc >= 19 and sexo == 1:
    falta = calc - 18
    print('Você tem {} anos já se passou {} anos do seu alistamento.'.format(calc, falta))
elif sexo == 2:
    print('Pessoas do sexo Feminino não tem a necessidade de comparecer ao alistamento obrigatório.')
