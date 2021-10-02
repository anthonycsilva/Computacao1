'''Questão Número: 1'''
def mult(matriz, multiplo):
    '''essa função recebe uma matriz e retorna ela multiplicada pelo numero que foi inserido'''
    '''list, int -> list'''
    resultado = list()
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])

    for i in range(qtd_linhas):
        resultado.append([])
        for j in range(qtd_colunas):
            mult = multiplo * matriz[i][j]
            list.append(resultado[i], mult)
    return resultado

'''Questão Número: 2'''
def ligou(lista,telefone):
    '''essa função recebe uma lista e pesquisa por um determinado telefone de pessoa, e retorna uma lista com as informações encontradas'''
    '''list, str -> list'''
    contatos_encontrados = list()

    for i in range(len(lista)):
        if (telefone in lista[i][1]):
            contatos_encontrados.append(lista[i])
    return contatos_encontrados