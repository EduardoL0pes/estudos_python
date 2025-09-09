c = 50
v = 20
d = 10
u = 1
while True:
    valor = int(input('Qual o valor a ser sacado? '))
    if valor > 50:
        valor /= c
    break
print(valor)