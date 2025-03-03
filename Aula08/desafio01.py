#Opção 01 SEM ENTRADA
"""from time import sleep

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
      '\nValor das parcelas: R${:.2f} '.format(emprestimo, salario, parcelas))"""

#Opção 02 COM ENTRADA
from time import sleep

casa = float(input('Digite o valor da casa: '))
salario = float(input('Seu salário: '))
parcela = int(input('Quantos anos de financiamento? '))
entrada = int(input('Valor de entrada: '))
print('\033[1;33mCALCULANDO EMPRÉSTIMO, POR FAVOR AGUARDE...\033[m')
sleep(2)
calc_parcela = casa / parcela / 12
calc_salario = salario * 30 / 100
if calc_parcela >= calc_salario and entrada == 0:
    print('Empréstimo \033[1;31mNEGADO\033[m!')
elif calc_salario >= calc_parcela and entrada == 0:
    print('Empréstimo \033[1;32APROVADO\033[m!')
elif entrada == entrada and entrada > 0:
    novo_calc_casa = casa - entrada
    novo_calc_parcela = novo_calc_casa / parcela / 12
    novo_calc_salario = salario * 30 / 100
    if novo_calc_parcela >= novo_calc_salario:
        print('Empréstimo \033[1;31mCOM ENTRADA NEGADO\033[m!')
    else:
        print('Empréstimo \033[1;32mCOM ENTRADA APROVADO\033[m!')
