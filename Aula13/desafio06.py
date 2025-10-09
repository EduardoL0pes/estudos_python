valores = []
ex = input('Digite uma expressão: ').strip()
valores.append(ex)

for c in range(len(valores)):
    analise = valores[c]
    if '()' in analise:
        print('Expressão está correta!')
    else:
        print('Expressão inválida.')

