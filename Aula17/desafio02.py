def fatorial(n, show=False):
    f = 1
    if show:
        num = n
        f = 1
        while num > 0:
            print(f'{num}', end='')
            print(' x ' if num > 1 else ' = ', end='')
            f *= num
            num -= 1
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f

print(fatorial(5, show=True))
