def ligou(lista,telefone):
    '''essa função recebe uma lista e pesquisa por um determinado telefone de pessoa, e retorna uma lista com as informações encontradas'''
    '''list, str -> list'''
    contatos_encontrados = list()

    for i in range(len(lista)):
        if (telefone in lista[i][1]):
            contatos_encontrados.append(lista[i])
    return contatos_encontrados
lista_contatos = list()

