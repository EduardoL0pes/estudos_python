from time import sleep


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')

    for v in num:
        sleep(0.4)
        print(f'{v}', end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')

maior(5,6,3,7,8,9)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)