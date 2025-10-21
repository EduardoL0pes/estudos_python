lista_alunos = list()

while True:
    test_nome = list()
    test_nome.append(input('Nome do aluno: ').strip().title())
    for n in range(2):
        test_nome.append(float(input(f'Nota {n+1}: ')))

    lista_alunos.append(test_nome)

    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print(f"{'No.':<4} {'NOME':<10} {'MÉDIA':>8}")
print('-'*25)
for i, aluno in enumerate(lista_alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f"{i:<2} {aluno[0]:<10} {media:>8.1f}")

while True:
    opc = int(input('\nMostra notas de qual aluno? (999 para sair): '))
    if opc == 999:
        break
    if opc < len(lista_alunos):
        aluno = lista_alunos[opc]
        print(f'Notas de {aluno[0]}: {aluno[1]} e {aluno[2]}')
    else:
        print('Aluno não encontrado!')