termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo_final = termo + (10-1) * razao
for c in range(termo, termo_final + razao, razao):
    print(c, end=' > ')
print('Acabou!')
