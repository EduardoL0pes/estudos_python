frase = 'Tentando Aprender Python'
#print(len(frase)) #24 caracteres

#Fatiamento
#print(frase[3]) #t
#print(frase[0:8]) #Tentando
#print(frase[0:25:2]) #Tnad pedrPto "pulando de 2 em 2"
#print(frase[:12]) #Tentando Apr "quando não se coloca o valor, se começa da primeira letra ate onde foi especificado terminar"
#print(frase[10:]) #prender Python "neste caso o valor de inicio foi especificado, mas não o valor de terminar com isso replicara toda frase restante"
#print(frase[0::3]) #TtdAeePh "quando se tem '::' proximo valor colocado depois desses pontos ira indicar a quantidade de letras a ser pulado nesse caso 3 em 3"

#Analise
#print(frase.count('n')) #quantidade de letras na frase nesse caso 4 letras
#print(frase.count('n', 0, 11)) #quantidade de letras, '0' onde começar, e '11' onde terminar. Neste caso 2 letras
#print(frase.find('Tentando')) #ira procurar a palavra especificada quando encontrada mostrara seu valor nesse caso 0
                              # se o valor for invalido mostrara -1 indicando que não foi encontrado
#print('Tentando' in frase) #de forma parecida com find ira procurar a palavra especificada, encontrada ira retornar true

#Transformação
#print(frase.replace('Tentando', 'Vou')) #procura a palavra e se encontrada substitui por outra especificada
#print(frase.upper()) #toda palavra em minuscula se torna maiuscula
#print(frase.lower()) #toda palavra em maiuscula se torna minuscula
#print(frase.capitalize()) #somente a primeira letra da frase ficara em maiuscula
#print(frase.title()) #ira analisar os espaços entre as palavras e colocara somente a primeira letra delas em maiuscula
#print(frase.strip()) #removera os espaços desnecessarios que houver no inicio e no final da frase
#print(frase.rstrip()) #remove os espaços a direita
#print(frase.lstrip()) #remove os espeços a esquerda

#Divisão
#print(frase.split()) #cada palavra na frase ficara numa lista e cada palavra tera seu 'numero' de inicio e termino, alem disso a frase inteira estara numa lista
#print('-'.join(frase)) #entre as letras ficara com esse '-'

""" Ex.:
frase = 'Curso em Video Python'.split()
print('-'.join(frase))

frase = 'Curso em Video Python'
print('-'.join(frase.split()))

Resultado de ambas: Curso-em-Video-Python 
"""

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. """) #para declaração de strings com 'varias' linhas
