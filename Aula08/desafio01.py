from time import sleep

print('\033[1;33mPor favor para confirmar sua aprovação de empréstimo me passe as seguintes informações para fazermos o calculo:\033[m')
emprestimo = float(input('Valor do empréstimo: R$'))
salario = float(input('Seu Salário: R$'))
anos = int(input('Quantos anos de financiamento: '))
print('\033[1;33mCALCULANDO EMPRÉSTIMO, POR FAVOR AGUARDE...\033[m')
sleep(2)

prestacao = anos * 12 #anos de financiamento a pagar
parcelas = emprestimo / prestacao #valor do emprestimo dividindo o tempo de financiamento
juros = salario * 30 / 100 #calculo do juros de 30%

if juros >= parcelas:
    print('\033[1;32mSeu empréstimo foi aprovado!\033[m')
else:
    print('\033[1;31mSeu empréstimo foi reprovado... O valor das parcelas ultrapassa os 30% do seu salário.\033[m')
print('-=-='*10)
print('Simulação do empréstimo: '
      '\nValor do empréstimo: R${:.2f} '
      '\nSalário do comprador: R${:.2f} '
      '\nValor das parcelas: R${:.2f} '.format(emprestimo, salario, parcelas))