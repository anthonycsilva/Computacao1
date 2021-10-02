def primo(n):
    '''essa função recebe se um é primo ou não '''
    '''int -> boolean '''
    divisores = list()
    for i in range(1, n+1):
        if n%i == 0:
            divisores.append(i)
    if len(divisores) > 2:
        return False
    else: 
        return True

print(primo(4))