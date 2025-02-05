#print(5+3*2) == 11
#print(3*5+4**2) == 31
#print(3*(5+4)**2) == 243

#nome = str(input('Qual é seu nome?'))
#print('Olá seja Bem Vindo {:=^20}!'.format(nome))
#print(f'Olá seja Bem Vindo {nome:=^20}!') ####F-Strings(uma forma mais abreviada)

n1 = int(input('Um valor'))
n2 = int(input('Outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {}, resto da divisao {} e a potência {}'.format(di, r, e))

#Obs: divisao{:.3f} >> para alterar a quantidade de casas a ser mostrado
#Quebra linha  -> \n
#continuar a frase na msm linha -> end=' '

#exemplo: print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d) end=' ')
