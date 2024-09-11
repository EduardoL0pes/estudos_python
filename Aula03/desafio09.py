salario = float(input('Digite seu salário: '))
aumento = salario * 15 / 100
novosalario = salario + aumento
print('Salário atual é de R${:.2f}, com aumento de 15% fica R${:.2f}, total acrescentado é de R${:.2f}'.format(salario, novosalario ,aumento))
