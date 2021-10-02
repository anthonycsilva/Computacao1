lista =[['Diego', '566','Anivia Supp','(21)9999999'],
        ['Clara', '566','Namorada','(21)9999999'],
        ['Samara', '566','Otaka','(21)9999999'],
        ['Vitória', '566','Gamer','(21)9999999']]


def busca(setor,matriz):
    '''essa função recebe uma matriz e retorna somente o nome daqueles que são de determinado setor'''
    '''str, list -> list'''
    setor = str.lower(setor)
    funcionarios_encontrados = []

    for i in range(len(matriz)) :
     if setor in str.lower(matriz[i][2]):
        cargo = matriz[i]
        del cargo[2]
        funcionarios_encontrados.append(cargo)
    return funcionarios_encontrados

print(busca('Namorada',lista))