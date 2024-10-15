print('\033[1;33mPor favor para confirmar sua aprovação de empréstimo me passe as seguintes informações para fazermos o calculo:\033[m')
emprestimo = float(input('Valor do empréstimo: '))
salario = float(input('Seu Salário: '))
parcela = int(input('Quantos anos para pagar: '))

div = emprestimo / parcela
exceder = salario * 30 / 100

if exceder > div:
    print('\033[1;32mSeu empréstimo foi aprovado!\033[m')
else:
    print('\033[1;31mSeu empréstimo foi reprovado\033[m')