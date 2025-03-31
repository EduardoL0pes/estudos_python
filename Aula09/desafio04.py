print('Tabuada 2.0')
tb = int(input('Tabuada de qual número?: '))
n = 0
for c in range(1, 10+1):
    c *= tb
    n += 1
    print(f'{tb}x{n} = {c}')