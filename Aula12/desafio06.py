palavras = 'aprender', 'estudar', 'escutar', 'linguagem', 'python', 'curso'
for p in palavras:  ##Percorre cada palavra na tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: ##Percorre cada letra na tupla
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')