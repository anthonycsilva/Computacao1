def eh_quadrada(matriz):
    '''essa função verifica se uma raiz é quadrada ou não '''
    '''list -> bool'''
    if matriz == []:
        return True
    else:
        qtd_linhas = len(matriz)
        qtd_colunas = len(matriz[0])

        if qtd_linhas == qtd_colunas:
            return True
        else:
            return False



print(eh_quadrada([[1,2,3],[4,5,6],[7,8,9]]))