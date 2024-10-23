from time import sleep

print('\033[31m-=-=\033[m'*10)
print('\033[1;33mCalculadora IMC\033[m')
print('\033[31m-=-=\033[m'*10)

peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
calc = round(peso / (altura * altura), 2)
print('\033[1;32mCALCULANDO IMC...\033[m')
sleep(2)
print(calc)
if calc <= 18.5:
    print('Você está abaixo do peso')
elif 18.5 < calc <= 25:
    print('Você está no peso ideal')
elif 25 < calc <= 30:
    print('Sobrepeso')
elif 30 < calc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

