print('-=' * 15)
print('Sequência de Fibonacci')
print('-=' * 15)
termo = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} > {t2} > ', end='')
while cont <= termo:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3} > ', end='')
    cont += 1
