diaria = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = (diaria * 60) + (kmrodado * 0.15)
print('Valor diário R${:.2f}, Km rodado R${:.2f}, Total a pagar R${:.2f}'.format(carro, kmrodado, total))
