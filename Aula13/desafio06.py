## Versão simples

# possui_parentes = 0
# ex = input('Digite uma expressão: ').strip()
#
# for c in ex:
#     if c == '(':
#         possui_parentes += 1
#     elif c == ')':
#         possui_parentes -= 1
#         if possui_parentes < 0:
#             break
#
# if possui_parentes == 0:
#     print('Expressão está correta!')
# else:
#     print('Expressão está incorreta.')

##Versão com pilha

ex = input('Digite uma expressão: ').strip()

pilha = []

for c in ex:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) == 0:
            print('Expressão está incorreta.')
            break
        else:
            pilha.pop()
else:
    if len(pilha) == 0:
        print('Expressão está correta!')
    else:
        print('Expressão está incorreta!')
#((a+b)*1)