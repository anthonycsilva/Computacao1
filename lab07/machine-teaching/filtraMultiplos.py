def filtraMultiplos(numeros, n):
    '''essa função recebe uma lista de numeros e retorna quais são deles são divisiveis por 'n' '''
    '''list,int -> list '''
    mult = list()
    i = int()

    while(i<len(numeros)):
        if(numeros[i]%n == 0):
            mult.append(numeros[i])

        i += 1

    return mult


filtraMultiplos([1,2,3,4,5,6,7,8],2)