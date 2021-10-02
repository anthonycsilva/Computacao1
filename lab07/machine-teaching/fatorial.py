def fatorial(n):
    '''essa função calcula o fatorial de um determinado numero '''
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat


print(fatorial(7))