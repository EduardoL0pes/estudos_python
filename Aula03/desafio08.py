preco = float(input('Digite o valor do produto R$'))
desconto = preco * 5 / 100  #desconto de 5%
novovalor = preco - desconto
print('Valor original do produto é R${:.2f}, com desconto de 5% fica R${:.2f}, total de desconto é de R${:.2f}'.format(preco, novovalor, desconto))
