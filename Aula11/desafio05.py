total_gasto = mais1000 = menor_valor = 0
menorn = ''
print('====Loja do Povão====')
while True:
    produto = input('Nome do produto: ')
    preco = int(input('Preço: R$'))
    conf = ' '
    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N]').upper().strip()[0]
    total_gasto += preco
    menor_valor += preco
    if menor_valor < preco:
        menorn = produto
    if preco > 1000:
        mais1000 += 1
    if conf == 'N':
        break
print(f'Quantidade de produtos que custam mais de R$1000: {mais1000}')
print(f'O nome do produto mais barato: {produto}')
print(f'Total gasto: R${total_gasto:.2f}')