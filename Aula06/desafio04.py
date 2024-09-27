distancia = float(input('Digite a distância percorrida: '))
if distancia <= 200:
    menor = distancia * 0.5
    print('A distância que irá percorrer/percorrida é de {:.0f}Km \n valor estimado para essa corrida é R${:.2f}'.format(distancia, menor))
else:
    maior = distancia * 0.4
    print('A distância que irá percorrer/percorrida é de {:.0f}Km \n valor estimado para essa corrida é de R${:.2f}'.format(distancia,maior))