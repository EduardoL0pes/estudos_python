def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=False))
help(fatorial)

# def fatorial(n, show=False):
#     f = 1
#     if show:
#         num = n
#         f = 1
#         while num > 0:
#             print(f'{num}', end='')
#             print(' x ' if num > 1 else ' = ', end='')
#             f *= num
#             num -= 1
#         return f
#     else:
#         for c in range(n, 0, -1):
#             f *= c
#         return f
#
# print(fatorial(5, show=True))
