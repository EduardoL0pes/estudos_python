#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz do número {} é {}'.format(num, math.ceil(raiz)))
#print(f'A raiz do número {num} é {raiz}')
# para importar toda biblioteca math

from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
#print('A raiz do número {} é {}'.format(num, ceil(raiz)))
print(f'A raiz do número {num} é {ceil(raiz)}')
# para importar somente os itens específicos de math ex: sqrt e ceil
