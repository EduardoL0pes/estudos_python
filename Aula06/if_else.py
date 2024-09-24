n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média é {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns você passou no teste!')
else:
    print('Infelizmente você reprovou, mas não desista!')