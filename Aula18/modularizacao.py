# from uteis import fatorial, dobro
from pacote import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O triplo de {num} é {numeros.triplo(num)}')