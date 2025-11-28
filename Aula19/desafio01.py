def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário não informou nenhum dado.\033[m')
            return 0
        else:
            return n


numi = leiaint('Digite um número inteiro: ')
numf = leiafloat('Digite um número real: ')
print(f'\033[34mVocê digitou o número INTEIRO {numi} e o número REAL {numf}\033[m')