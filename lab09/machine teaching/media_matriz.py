def media_matriz(matriz):
    '''essa funçao recebe uma matriz e soma todos os numeros e tira sua média'''
    '''list -> float'''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])

    soma = 0
    contador = 0

    for i in range(qtd_linhas):
        for l in range(qtd_colunas):
            soma = soma + matriz[i][l]
            contador +=1
    return round(soma/contador, 2)


print(media_matriz([[1,2],[4,5]]))
#1,2,4,5 media = 3