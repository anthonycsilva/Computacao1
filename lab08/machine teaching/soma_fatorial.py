import math
def soma_fatorial(n):
    '''essa função retorna a soma das fatoriais de um numero n '''
    '''int -> int'''
    soma_fator = list()
    for i in range(1,n+1):
        soma_fator.append(math.factorial(i))

    return sum(soma_fator)
print(soma_fatorial(1))