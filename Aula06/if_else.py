n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Parabéns você foi aprovado! \n Média final: {m}' if m>=6 else 'Infelizmente você foi reprovado.') #Forma mais simplificada, para condições mais simples

"""if m >= 6.0:
    print('Parabéns você passou no teste!')
else:
    print('Infelizmente você reprovou, mas não desista!')"""

#---------------------------------

print("""Olá, vamos realizar uma continha de adição:
Quanto é 5 + 2?""")
print(f'{'':-^20}')
res = float(input('Escreva sua resposta: '))
if res == 7:
    print('Parabéns você ACERTOU!!')
else:
    print('Você ERROU! :/')
print(f'{'FIM':-^20}')
#Voltarei para implementar loop 
