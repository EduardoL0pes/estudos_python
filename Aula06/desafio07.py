salario = float(input('Digite seu salário: R$'))
if salario >= 1250:
    sup = salario * 10 / 100 #Salário superior a R$1.250
    novo = salario + sup
    print('Seu novo salário com 10% de aumento fica R${:.2f} com um aumento de R${:.2f}'.format(novo, sup))
else:
    inf = salario * 15 / 100 #Salário inferior a R$1.250
    novo = salario + inf
    print('Seu novo salário com 15% de aumento fica R${:.2f} com um aumento de R${:.2f}'.format(novo, inf))
