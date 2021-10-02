def insere(lista_numero,n):
#essa função recebe uma lista de numero e colocar o numero 'n' de forma ordenada e retorna a lista em ordem
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero 

print(insere([8,2,6,4,4], 3))
