def metade(v):
    res =  v / 2
    return res

def dobro(v):
    res = v * 2
    return res

def aumentar(v, taxa):
    res = (v * taxa / 100) + v
    return res

def diminuir(v, taxa):
    res = v - (v * taxa / 100)
    return res