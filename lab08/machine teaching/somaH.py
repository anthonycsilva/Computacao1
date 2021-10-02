def soma_h(n):
    '''essa função recebe um numero e retorna a soma da divisão de 1/1 até 1/n'''
    '''int -> float '''
    h = 1
    for i in range(2, n+1):
        h = h+(1/i)
    return round(h,2)

print(soma_h(10))