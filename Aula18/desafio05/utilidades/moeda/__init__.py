def metade(p=0, formato=False):
    res = p / 2
    return res if formato is False else moeda(res)

def dobro(p=0, formato=False):
    res = p * 2
    return res if formato is False else moeda(res)

def aumentar(p=0, taxa=0, formato=False):
    res = p + (p * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(p=0, taxa=0, formato=False):
    res = p - (p * taxa / 100)
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(valor, ataxa=10, dtaxa=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'\033[1;34mAnalise do valor: {moeda(valor)}\033[m')
    print(f'Metade: \t\t{metade(valor, True)}')
    print(f'Dobro: \t\t\t{dobro(valor, True)}')
    print(f'Aumento de {ataxa}%: {aumentar(valor, ataxa, True)}')
    print(f'Redução de {dtaxa}%: {diminuir(valor, dtaxa, True)}')
    print('-'*30)