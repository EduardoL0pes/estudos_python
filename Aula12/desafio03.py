#Opção01
# import random
#
# num_tup = tuple(random.randint(0,10) for c in range(5))
# print(f'{num_tup} \n', end='')
# print(f'O maior número sorteado: {max(num_tup)}')
# print(f'O menor número sorteado: {min(num_tup)}')


#Opção02
from random import randint

numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados são: ', end='')
for n in numero:
    print(f'{n}', end=' ')
print(f'\nO maior número sorteado: {max(numero)}')
print(f'O menor número sorteado: {min(numero)}')