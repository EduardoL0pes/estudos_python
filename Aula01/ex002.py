nome = input('Qual é seu nome?')
idade = input('Qual sua idade?')
peso = input('Qual seu peso?')
if peso >= '80':
    acimaMedia = 'Você esta gordo'
    print('bem vindo', nome, 'você tem', idade, 'anos e pesa', peso, 'kilos', ',',acimaMedia, '!!!')
else:
    print('bem vindo', nome, 'voce tem', idade, 'anos e pesa', peso, 'kilos')