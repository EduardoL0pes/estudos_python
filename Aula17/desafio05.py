def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor original, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r

resp = notas(5.5,2.5,8.5, sit=True)
print(resp)
help(notas)


# def notas(*n, sit=False):
#     """
#     Tentei..
#     :param n: recebe varios valores números.
#     :param sit: mostrar ou não a situação do aluno (Aprovado,Recuperação,Reprovado)
#     :return: Retorna o dicionario com as informações do aluno
#     """
#     dic = dict()
#     dic['aluno'] = n
#
#     media = sum(dic['aluno'])
#
#     maior = menor = 0
#     for v in dic.values():
#         if v != 0:
#             maior = max(v)
#             menor = min(v)
#     dic['maior'] = maior
#     dic['menor'] = menor
#
#     dic['média'] = media / len(dic['aluno'])
#     dic['total de notas'] = len(dic['aluno'])
#
#     if sit:
#         if dic['média'] >= 7:
#             dic['situação'] = 'APROVADO!'
#         elif 5 <= dic['média'] <= 6.9:
#             dic['situação'] = 'RECUPERAÇÃO...'
#         elif dic['média'] <= 4.9:
#             dic['situação'] = 'REPROVADO!!'
#
#     return dic
#
# resp = notas(5.5,2.5,10,6.5, sit=True)
# print(resp)
#
# help(notas)
