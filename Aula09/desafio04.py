print('Tabuada 2.0')
#Opção I
"""tb = int(input('Tabuada de qual número?: '))
n = 0
for c in range(1, 11):
    c *= tb
    n += 1
    print(f'{tb}x{n} = {c}')"""

#Opção II
tb = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print(f'{tb}x{c} = {tb*c}')