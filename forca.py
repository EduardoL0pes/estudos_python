from random import choice

palavras = ['claustrofobia', 'aprender']
palavra_secreta = choice(palavras)
letras_descobertas = ['_'] * len(palavra_secreta)
vidas = 6

while vidas > 0 and '_' in letras_descobertas:
    print('Palavra:', ' '.join(letras_descobertas))
    print(f'Vidas restantes: {vidas}')

    letra = input('Digite uma letra: ').strip().lower()
    if len(letra) != 1 or not letra.isalpha():
        print('Por favor, digite uma única letra.')
        continue

    if letra in palavra_secreta:
        print('Boa! A letra está na palavra.')
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        print('Errou! Tente outra letra')
        vidas -= 1

    print('-' * 30)

if '_' not in palavra_secreta:
    print('PARABÉNS! Você ganhou!')
    print(f'A palavra era: {palavra_secreta}')
else:
    print('GAME OVER! Você perdeu!')
    print(f'A palavra era: {palavra_secreta}')