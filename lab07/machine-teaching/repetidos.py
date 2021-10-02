def repetidos(numeros):
    '''essa função recebe uma lista de numeros e retorna quando numeros são iguais aos seus antecessores'''
    '''list -> int'''
    i = int()
    cont = int()
    tamanho = len(numeros)
    while i<tamanho:
        if(numeros[i] == numeros[i-1]):
            cont +=1
        i +=1


    return cont


print(repetidos([1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]))