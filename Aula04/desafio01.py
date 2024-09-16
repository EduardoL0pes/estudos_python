from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
#podendo usar tbm no lugar do TRUNC a função int(), com isso não irá precisar importa a biblioteca math