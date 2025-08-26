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
print('Acabou!')