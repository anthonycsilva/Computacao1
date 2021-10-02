def filtra_pares(tupla):
    pares = ()
    n = 0

    while(n<= len(tupla)-1):
        if(tupla[n]%2 == 0):
            pares += (tupla[n],)
        else:
            print(f'O Numero {tupla[n]}, não é par')
        n = n+1

    return print(f'Os numeros pares são: {pares}')

filtra_pares((1,2,4,2,1,25,6,3,46,3,2,4,5,76,67,3,2,34,5,6,34,2))