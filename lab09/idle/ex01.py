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


print(mult([[1,8,-3],[4,-2,5]],2))