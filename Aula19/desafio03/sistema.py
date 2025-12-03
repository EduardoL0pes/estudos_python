from time import sleep
from lib.arquivo import *
from lib.interface import *

arq = 'cadastro.txt'

if not aqruivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        ler_arquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ').title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: por favor, digite uma opção válida.\033[m')
    sleep(1)