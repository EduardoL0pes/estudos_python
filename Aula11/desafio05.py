total_gasto = mais1000 = menor_valor = cont = 0
menorn = ' '
print('====Loja do Povão====')
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1 or preco < menor_valor: #Simplificada
        menor_valor = preco
        menorn = produto
    # else:
    #     if preco < menor_valor:
    #         menor_valor = preco  #Detalhada
    #         menorn = produto
    conf = ' '
    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N]').upper().strip()[0]
    if conf == 'N':
        break
print('{:-^40}'. format('Fim do programa'))
print(f'Quantidade de produtos que custam mais de R$1000.00: {mais1000}')
print(f'O nome do produto mais barato foi {menorn} que custa R${menor_valor:.2f}')
print(f'Total gasto: R${total_gasto:.2f}')
