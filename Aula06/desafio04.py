from time import sleep
distancia = float(input('Digite a distância que irá percorrer: '))
print('CALCULANDO DISTÂNCIA...')
sleep(2)
if distancia <= 200:
    menor = distancia * 0.50
    print('A distância que irá percorrer/percorrida é de {:.0f}Km \n valor estimado para essa corrida é R${:.2f}'.format(distancia, menor))
else:
    maior = distancia * 0.45
    print('A distância que irá percorrer/percorrida é de {:.0f}Km \n valor estimado para essa corrida é de R${:.2f}'.format(distancia,maior))
