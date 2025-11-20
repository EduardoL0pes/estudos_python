def pyhelp():
    print('-'*30)
    print('SISTEMA DE AJUDA PyHELP'.center(30))
    print('-'*30)

    while True:
        help(input('Função ou Biblioteca > '))

        if help == 'fim':
            break

pyhelp()
