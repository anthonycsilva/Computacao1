def posLetra(frase,letra,ocorrencia):
    '''essa função recebe uma frase, uma letra, a ocorrencia. e retorna em qual casa está a ocorrencia escolhida'''
    frase = list(frase)
    i = int()
    occ = int()
    while i<len(frase):
        if(frase[i] == letra):
            occ += 1
            if(occ == ocorrencia):
                return i
        i +=1
    if(occ < ocorrencia):
            return -1

    



print(posLetra('Marin come bnna','a',2))