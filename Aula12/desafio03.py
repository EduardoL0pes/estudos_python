import random

num_tup = tuple(random.randint(0,10) for c in range(5))
print(f'{num_tup} \n', end='')
print(f'O maior número sorteado: {max(num_tup)}')
print(f'O menor número sorteado: {min(num_tup)}')
