salario = float(input('Digite seu salário: '))
if salario >= 1250:
    sup = salario * 10 / 100 #Salários superiores a R$1.250
    novo = salario + sup
    print('Seu salário novo é R${:.2f} com um aumento de R${:.2f}'.format(novo, sup))
else:
    inf = salario * 15 / 100 #Salários inferiores a R$1.000
    novovalor = salario + inf
    print('Seu novo salário com aumento de 15% é R${:.2f} com um aumento de R${:.2f}'.format(novovalor, inf))