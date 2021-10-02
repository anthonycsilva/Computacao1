def busca_contato2(lista,nome):
    '''essa função recebe uma lista e pesquisa por um determinado nome de pessoa, e retorna uma lista com as informações encontradas'''
    '''list, str -> list'''
    nomes_encontrados = list()

    for i in range(len(lista)):
        if (nome in lista[i][0]):
            nomes_encontrados.append(lista[i])
    return nomes_encontrados






