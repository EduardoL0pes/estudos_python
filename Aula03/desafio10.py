f = float(input('Digite a temperatura em Fahrenheit: '))
cel = (f - 32) / 1.8
celsius = float(input('Digite a temperatura em Celsius: '))
fah = celsius * 1.8 + 32
print('A temperatura em Fahrenheit é de {:.0f}°F, convertendo para Celsius fica {:.0f}°C'.format(f, cel))
print('A temperatura em Celsius é {:.0f}°C, convertendo para Fahrenheit fica {:.0f}°F'.format(celsius, fah))
