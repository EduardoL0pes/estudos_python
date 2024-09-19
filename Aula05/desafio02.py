n = int(input('Digite um número: '))
mi = n // 1000 % 10
ce = n // 100 % 10
de = n // 10 % 10
un = n // 1 % 10
print("""
unidade:{}
dezena:{}
centena:{}
milhar:{}""".format(un, de, ce, mi))