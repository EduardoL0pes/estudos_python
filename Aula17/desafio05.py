def notas(*n, sit=False):
    dic = dict()
    dic['aluno'] = n

    dic['total de notas'] = len(dic['aluno'])


    return dic

resp = notas(5,6,7)
print(resp)