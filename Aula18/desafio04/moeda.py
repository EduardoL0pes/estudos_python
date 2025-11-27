def metade(p, formato=False):
    res = p / 2
    return res if formato is False else moeda(res)

def dobro(p=0, formato=False):
    res = p * 2
    return res if not formato else moeda(res)

def aumentar(p=0,taxa=0, formato=False):
    res = p + (p * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(p=0, taxa=0, formato=False):
    res = p - (p * taxa / 100)
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, ataxa=10, dtaxa=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Aumento de {ataxa}%: \t{aumentar(preco, ataxa, True)}')
    print(f'Redução de {dtaxa}%: \t{diminuir(preco, dtaxa, True)}')
    print('-'*30)