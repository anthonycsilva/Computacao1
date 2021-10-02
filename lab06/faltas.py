def faltas(times):
#essa função recebe uma lista de times com numeros de faltas, e retorna o total de faltas do campeonato inteiro
    faltas_jogo1 = times[0][2][0] + times[0][2][1]
    faltas_jogo2 = times[1][2][0] + times[1][2][1]
    faltas_jogo3 = times[2][2][0] + times[2][2][1]
    return faltas_jogo1 + faltas_jogo2 + faltas_jogo3


faltas([['Brasil','Italia',[10,9]],['Brasil','Espanha',[5,7]],['Italia','Espanha',[7,8]]])
