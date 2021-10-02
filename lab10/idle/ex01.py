import random

def dado():
    '''essa função gera numeros aleatórios de um dado e os coloca em uma lista'''
    '''->list'''
    lista_numeros = list()
    i = 0
    n = int(input('Quantos Numeros deseja?'))
    while i<n:
        numero = random.randint(1,6)
        lista_numeros.append(numero)
        i+= 1
    print(lista_numeros)
    return lista_numeros



def conta_faces(lista):
    '''essa função conta quantas faces do dado apareceram durante a execução da função dado'''
    ''' list -> int '''
    resultado = list()
    for i in range(len(lista)):
        if lista[i-1] == lista[i] and lista[i] != lista[i+1]:
            resultado.append(lista[i])
    print(len(resultado))
    return resultado


conta_faces(dado())