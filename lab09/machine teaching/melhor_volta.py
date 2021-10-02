def melhor_volta(matriz):
    '''essa função recebe uma matriz com resultados de uma corrida, e retorna o vencedor, o melhor tempo e em qual corrida foi o melhor tempo'''
    '''list -> tuple'''
    qtd_linhas = len(matriz)
    resultado = 10000
    coluna = 0
    for i in range(qtd_linhas):
        melhor_tempo = min(matriz[i])
        if resultado > melhor_tempo:
             resultado = melhor_tempo
             print(resultado)
             corredor = i
             coluna = matriz[i].index(melhor_tempo)     

    return corredor+1, resultado,coluna




print(melhor_volta([[74,77,57,35,66,22,46,55,7,79],
                    [20,62,93,6,67,85,1,11,49,76],
                    [84,44,87,27,19,43,56,29,86,63],
                    [12,61,92,40,8,60,13,68,23,98],
                    [45,18,47,10,70,9,69,2,36,14],
                    [94,47,15,39,91,80,21,58,48,24]]))


#return(2,1,6)