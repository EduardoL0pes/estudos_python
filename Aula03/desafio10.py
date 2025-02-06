f = float(input('Informe a temperatura em Fahrenheit: '))
cel = (f - 32) / 1.8
celsius = float(input('Informe a temperatura em Celsius: '))
fah = celsius * 1.8 + 32
print('A temperatura de {:.0f}°F corresponde a {:.0f}°C'.format(f, cel))
print('A temperatura de {:.0f}°C corresponde a {:.0f}°F'.format(celsius, fah))
