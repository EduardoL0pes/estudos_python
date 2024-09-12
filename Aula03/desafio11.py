diaria = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
carro = diaria * 60
kmrodado = km * 0.15
total = carro + kmrodado
print('Valor diário R${:.2f}, Km rodado R${:.2f}, Total a pagar R${:.2f}'.format(carro, kmrodado, total))