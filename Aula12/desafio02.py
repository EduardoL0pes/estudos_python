times = ('flamengo', 'cruzeiro', 'palmeiras', 'mirassol', 'botafogo',
         'bahia', 'são paulo', 'fluminense', 'bragantino', 'corinthians',
         'ceará', 'grêmio', 'internacional', 'santos', 'atlético-MG',
         'vasco', 'vitória', 'juventude', 'fortaleza', 'sport')
print(f'Os 5 primeiros colocados: {times[:5]}')
print(f'Os 4 últimos: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'O time do {times[7]} esta em {times.index('fluminense')+1}ª posição')
