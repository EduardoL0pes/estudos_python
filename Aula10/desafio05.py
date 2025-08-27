#Definindo os parâmetros de PA
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
qt_termos = 10
#Inicializando variáveis
contador = 0
termo_atual = termo
#Gerando PA
print('Progressão Aritmética')
while contador < qt_termos:
    print(termo_atual, end=' > ')
    termo_atual += razao #Calcula o próximo termo
    contador += 1  #Incrementa o contador

res = input('Deseja continar a progressão? [S/N] ').upper
if res == 'S':
    nv_termos = 20
    while termo_atual < nv_termos:
        print(termo_atual, end=' > ')
        termo_atual += razao
        contador += 1