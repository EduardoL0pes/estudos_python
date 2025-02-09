from random import sample
alunos = 'Eduardo', 'Ricardo', 'Matheus', 'Priscila'
gerador = sample(alunos, k=4)
print('A ordem de apresentação dos alunos será {}'.format(gerador))
