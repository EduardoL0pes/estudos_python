import math
oposto = float(input('Digite o valor do cat. oposto: '))
ad = float(input('Digite o valor do cat. adjacente: '))
mult = pow(oposto,2) + pow(ad,2)
hipo = math.sqrt(mult)
print('O comprimento da Hipotenusa é {}'.format(hipo))