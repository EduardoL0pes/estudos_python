oposto = float(input('Digite o valor do cat. oposto: '))
ad = float(input('Digite o valor do cat. adjacente: '))
hipo = (pow(oposto,2) + pow(ad,2)) ** (1/2)
print('O valor da Hipotenusa é {:.2f}'.format(hipo))