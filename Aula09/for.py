"""OBS:for c in range(0,6):
    print(c)"""     #Esse 'c' é a variável, podendo ser qualquer outro nome da nossa escolha
#Res: 0,1,2,3,4,5

#exemplo 01
"""for c in range(1,10):
    passo
pega"""

#exemplo 02
"""for c in range(0,3):
        if coin:
            pega
    passo
    pula
passo
pega"""

#exemplo 03
"""for c in range(6, 0, -1):
    print(c)        
print('fim')"""     #Contagem regressiva

#exemplo 04
"""for c in range(1, 6):
    print('oi')  o
print('fim')"""     #contagem de 1 a 5 'oi' pois no 6 ele para a execuçã

#exemplo 05
"""for c in range(0,7,2):
    print(c)"""    #contagem de 0 a 6 pulando de 2 em 2 (lembrando que o num 7 ele para a execução)

#exemplo 06
"""n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)  """          #contagem de 1 á 3 ('n+1' para mostrar o num 3 no final do programa, senão a contagem mostraria somente 0,1,2)
#Res: 0,1,2,3

#exemplo 07
"""i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)"""
#Interativo, exemplo que i = 0, f = 10, p = 2
#Contagem do inicio 0, chegando ao fim 10, pulando de 2 em 2
#Res 0,2,4,6,8,10

#exemplo 08
"""for c in range(0, 3):
    n = int(input('Digite um número: '))
print('Fim')"""
#A execução da variável 'n' acontecerá 3 vezes
#Res n = int(input('Digite um número: '))
    #n = int(input('Digite um número: '))
    #n = int(input('Digite um número: '))

#exemplo 09
"""s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n  #s = s + n
print(f'A somatória de todos os valores é igual a {s}')"""
#Irá executar 4 vezes a variável 'n' depois mostrará a soma de todos os valores representado na variável 's'
#Res supondo que eu escolha no input esses valores: 1+2+3+4 = 10