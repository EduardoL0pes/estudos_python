def notas(*n, sit=False):
    """
    Tentei..
    :param n: recebe varios valores números.
    :param sit: mostrar ou não a situação do aluno (Aprovado,Recuperação,Reprovado)
    :return: Retorna o dicionario com as informações do aluno
    """
    dic = dict()
    dic['aluno'] = n

    media = sum(dic['aluno'])

    maior = menor = 0
    for v in dic.values():
        if v != 0:
            maior = max(v)
            menor = min(v)
    dic['maior'] = maior
    dic['menor'] = menor

    dic['média'] = media / len(dic['aluno'])
    dic['total de notas'] = len(dic['aluno'])

    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'APROVADO!'
        elif 5 <= dic['média'] <= 6.9:
            dic['situação'] = 'RECUPERAÇÃO...'
        elif dic['média'] <= 4.9:
            dic['situação'] = 'REPROVADO!!'

    return dic

resp = notas(5,9,7, sit=True)
print(resp)

help(notas)
