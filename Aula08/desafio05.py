nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
res = (nota1 + nota2) / 2

if res <= 4.9:
    print('Sua média final é \033[1;31m{}\033[m, você foi \033[1;31mREPROVADO!\033[m'.format(res))
elif res >= 5  <= 6.9:
    print('Sua média final é \033[1;33m{}\033[m, você foi para \033[1;33mRECUPERAÇÃO\033[m'.format(res))
elif res >= 7:
    print('Sua média final é \033[1;32m{}\033[m, PARABÉNS VOCÊ FOI \033[1;32mAPROVADO!!!\033[m'.format(res))