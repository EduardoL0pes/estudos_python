from utilidades import moeda
from utilidades import dado

p = dado.leia_dinheiro('Digite um preço: R$')
moeda.resumo(p, 50, 40)