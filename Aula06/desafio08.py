r1 = int(input('Digite o primeiro valor: '))
r2 = int(input('Digite o segundo valor: '))
r3 = int(input('Digite o terceiro valor: '))
soma = r1 + r2
if soma > r3:
    print('Pode se formar um triângulo \n valor da soma de {} + {} = {} > {}'.format(r1, r2, soma, r3))
else:
    print('Não pode formar um triângulo \n valor da soma de {} + {} = {} < {}'.format(r1, r2, soma, r3))