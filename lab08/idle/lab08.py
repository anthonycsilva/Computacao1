import math
def soma(n):
     ''' essa função realiza uma soma de aproximação de pi/4, N vezes '''
     ''' int -> float '''
     somas = 0
     for i in range(n+1):
         somas += ((-1)**i)/(2*i+1)
     return somas

def erro():
    '''essa função executa a soma até o numero que se aproxima de 0.01'''
    ''' -> tuple  '''
    numero = 0
    while not math.fabs(soma(numero)-(math.pi)/4)<0.01:
        numero += 1
    return (numero, soma(numero))


''' Numero 2 '''


def busca_contato2(lista,nome):
    '''essa função recebe uma lista e pesquisa por um determinado nome de pessoa, e retorna uma lista com as informações encontradas'''
    '''list, str -> list'''
    nomes_encontrados = list()

    for i in range(len(lista)):
        if (nome in lista[i][0]):
            nomes_encontrados.append(lista[i])
    return nomes_encontrados
