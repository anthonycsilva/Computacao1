def eh_ordenada(numeros):
#essa função verifica se, dado uma lista de numeros, se estão ordenados ou não, e em qual ordem, crescente ou decrescente
    numeros_crescentes = sorted(numeros)
    numeros_DEcrescentes = sorted(numeros, reverse=True)

    if(numeros_crescentes == numeros):
        return (True,'crescente')
    if(numeros_DEcrescentes == numeros):
        return (True,'decrescente')
    if (numeros_crescentes != numeros and numeros_DEcrescentes != numeros):
        return (False,'desordenada')

print(eh_ordenada([19,18,12,8,7,6,5,4]))