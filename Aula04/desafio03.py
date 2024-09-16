from math import radians, sin, cos, tan
num = int(input('Digite um valor: '))
convert = radians(num)
seno = sin(convert)
cos = cos(convert)
tan = tan(convert)
print('O valor seno de {}° é igual {:.2f}'.format(num, seno))
print('O valor cosseno de {}° é igual {:.2f}'.format(num,cos))
print('O valor tangente de {}° é igual {:.2f}'.format(num, tan))