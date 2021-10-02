def conta_numero(numero,matriz):
    '''essa função recebe um numero e uma matriz, e retorna quantas vezes esse numero foi repetido na matriz'''
    '''int, list -> int'''
    if matriz == []:
        return 0
    else:
        qtd_linhas = len(matriz)
        qtd_colunas = len(matriz[0])
        contador = 0

        for i in range(qtd_linhas):
            for l in range(qtd_colunas):
                if matriz[i][l] == numero:
                    contador +=1
        return contador


print(conta_numero(2,[[1,2,4,5,7],[2,4,2,1,2]]))