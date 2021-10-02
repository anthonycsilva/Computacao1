def ordena_por_insercao(lista):
    '''essa função recebe uma lista e retorna ela feita pelo método de inserção'''
    '''list -> list'''
    for i in range(1, len(lista)):
        valorAtual = lista[i]
        posAtual = i

        while posAtual > 0 and lista[posAtual - 1] > valorAtual:
            lista[posAtual] = lista[posAtual -1]
            posAtual-=1

        lista[posAtual] = valorAtual
        lista.append(valorAtual)

    return lista