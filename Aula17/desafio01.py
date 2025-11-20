def voto(nasc):
    from datetime import date
    data = date.today().year
    calc = data - ano

    print(f'Você tem {calc} anos.')
    if 18 <= calc <= 59:
        return 'VOTO OBRIGATÓRIO!'
    if calc >= 60:
        return 'VOTO OPCIONAL'
    if calc <= 17:
        return 'NÃO PODE VOTAR'


ano = int(input('Ano de nascimento: '))
print(voto(ano))
