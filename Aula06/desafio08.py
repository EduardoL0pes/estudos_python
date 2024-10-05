from time import sleep

r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
soma = r1 + r2
print('=-=-' * 10)
print('Calculando Valores...')
print('=-=-' * 10)
sleep(2)
if soma > r3:
    print('Valor da soma de {} + {} = {} se for > {} \n Podem se formar um triângulo '.format(r1, r2, soma, r3))
else:
    print('valor da soma de {} + {} = {} se for < {} \n Não podem formar um triângulo'.format(r1, r2, soma, r3))

"""OBS: O resultado da soma de r1 + r2 não pode ser menor que r3"""