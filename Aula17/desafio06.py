from time import sleep

c = ['\033[m',         # 0 - sem cores
    '\033[0;30;41m',   # 1 - vermelho
    '\033[0;30;42m',   # 2 - verde
    '\033[0;30;44m',   # 3 - azul
    '\033[7;40m'       # 4 - branco
]

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',3)
    sleep(0.5)
    print(c[4], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO',1)