# lista_alunos = list()
#
# while True:
#     test_nome = list()
#     test_nome.append(input('Nome do aluno: ').strip().title())
#     for n in range(2):
#         test_nome.append(float(input(f'Nota {n+1}: ')))
#
#     lista_alunos.append(test_nome)
#
#     resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break
#
# print(f"{'No.':<4} {'NOME':<10} {'MÉDIA':>8}")
# print('-'*25)
# for i, aluno in enumerate(lista_alunos):
#     media = (aluno[1] + aluno[2]) / 2
#     print(f"{i:<2} {aluno[0]:<10} {media:>8.1f}")
#
# while True:
#     opc = int(input('\nMostra notas de qual aluno? (999 para sair): '))
#     if opc == 999:
#         break
#     if opc < len(lista_alunos):
#         aluno = lista_alunos[opc]
#         print(f'Notas de {aluno[0]}: {aluno[1]} e {aluno[2]}')
#     else:
#         print('Aluno não encontrado!')


# Opção02
ficha = list()

while True:
    nome = input('Nome: ').strip(). title()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resp = input('Deseja continuar? [S/N] ')
    if resp in 'Nn':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')