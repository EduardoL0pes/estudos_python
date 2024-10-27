nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
res = (nota1 + nota2) / 2

if res <= 4.9:
    print('Sua média final é \033[1;31m{:.1f}\033[m, aluno foi \033[1;31mREPROVADO.\033[m'.format(res))
elif 5 <= res < 7:
    print('Sua média final é \033[1;33m{:.1f}\033[m, aluno foi para \033[1;33mRECUPERAÇÃO.\033[m'.format(res))
elif res >= 7:
    print('Sua média final é \033[1;32m{:.1f}\033[m, PARABÉNS O ALUNO FOI \033[1;32mAPROVADO.\033[m'.format(res))
