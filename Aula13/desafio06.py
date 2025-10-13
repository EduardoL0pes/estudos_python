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
# ex = input('Digite uma expressão: ').strip()
#
# pilha = []
#
# for c in ex:
#     if c == '(':
#         pilha.append('(')
#     elif c == ')':
#         if len(pilha) == 0:
#             print('Expressão está incorreta.')
#             break
#         else:
#             pilha.pop()
# else:
#     if len(pilha) == 0:
#         print('Expressão está correta!')
#     else:
#         print('Expressão está incorreta!')

#((a+b)*1)

#Opção02
expr = input('Digite a expressão: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:  #Verifica se a pilha é maior que zero se for quer dizer que fechou o '()'
            pilha.pop()     #então ele remove o parenteses aberto fechando assim seu par
        else:
            pilha.append(')')  #Senão tem algum parenteses errado ou ')' a mais, fazendo assim um break do programa e dando erro
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
