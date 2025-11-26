def metada(p=0):
    res = p / 2
    return res

def dobro(p=0):
    res = p * 2
    return res

def aumentar(p=0, taxa=0):
    res = p + (p * taxa / 100)
    return res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')