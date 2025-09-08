total_gasto = mais_caro = menor_valor = 0
barato = ''
print('====Loja do Povão====')
while True:
    produto = input('Nome do produto: ')
    preco = int(input('Preço: R$'))
    conf = input('Deseja continuar? [S/N]').upper().strip()
    while conf == 'S':
        menor_valor = preco
        total_gasto += preco
        if preco >= 1000:
            mais_caro += 1
        if preco < menor_valor:
            barato = produto
        break

    print(f'{produto}, R${preco} QT mais caro >> {mais_caro} total >> {total_gasto} menor valor >> {barato}')