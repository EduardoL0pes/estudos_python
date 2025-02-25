from datetime import date
ano = int(input('Que ano deseja analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #analisa ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é bissexto'.format(ano))
else:
    print('Ano {} não é bissexto'.format(ano))
