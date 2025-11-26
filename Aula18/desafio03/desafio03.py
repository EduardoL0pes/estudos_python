import moeda

p = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metada(p))}')
print(f'O doblro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')