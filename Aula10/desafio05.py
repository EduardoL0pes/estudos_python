#Opção1
# # Definindo os parâmetros de PA
# termo = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# qt_termos = 10
# # Inicializando variáveis
# contador = 0
# termo_atual = termo
# # Gerando PA
# print('Progressão Aritmética')
# while contador < qt_termos:
#     print(termo_atual, end=' > ')
#     termo_atual += razao  # Calcula o próximo termo
#     contador += 1  # Incrementa o contador
# print('FIM')

#Opção2
print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão do PA: '))
qt_termos = termo
cont = 1

while cont <= 10:
    print(f'{termo} > ', end=' ')
    termo += razao
    cont += 1
print('FIM')