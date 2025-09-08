maiores = 0
masc = 0
fem = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: [M/F] ').upper().strip()
    conf = input('Deseja continuar o cadastro? [S/N] ').upper().strip()
    if conf == 'S':
        if idade >= 18:
            maiores += 1
        if sexo == 'M':
            masc += 1
        if sexo == 'F' and idade < 20:
            fem += 1
    else:
        print('----FIM DO PROGRAMA----')
        print(f'Um total de {maiores} pessoas foram cadastradas.')
        print(f'Foram cadastrados {masc} homens.')
        print(f'E um total de {fem} mulheres com menos de 20 anos.')
        break
