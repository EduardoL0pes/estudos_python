# def mostralinha(): #Def (definição de função)
#     print('-'*25)
#
# mostralinha()
# print('HELLO WORLD'.center(25))
# mostralinha()

# def mensagem(msg):
#     print('-'*25)
#     print(msg.center(25))
#     print('-'*25)
#
# mensagem('APRENDENDO SOBRE FUNÇÕES')
# mensagem('LINGUAGEM PYTHON')
# mensagem('HELLO WORLD')

# def soma(a, b): #Parametro
#     s = a + b
#     print(s)
#
# #Programa principal
# soma(4,5)
# soma(8,9)
# soma(2,1)
# soma(b=2,a=1) #Podendo tambem trocar a ordem dos parametros entre b e a


# Empacotamento
# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números.')
#
# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)


# def contador(*num):
#     for valor in num:
#         print(f'{valor}', end=' ')
#
# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)


#Listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)