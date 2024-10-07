print('\033[1;7;40mHello, World!\033[m')
print('\033[1;36;40mTestando\033[m')
print('\033[7;31;44m=-=-\033[m'*10)

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Eduardo'
print('Prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'pretoebranco': '\033[7;40m'}

print('Seja bem vindo, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))