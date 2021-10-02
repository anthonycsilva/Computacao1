import random
def geradorCampo():
    campo = [[0 for linha in range(9)] for coluna in range(9)]
    for num in range(10):
        x = random.randint(0,8)
        y = random.randint(0,8)
        campo[y][x] = 'X'
        if (x >=0 and x <= 9-2) and (y >= 0 and y <= 9-1):
            if campo[y][x+1] != 'X':
                campo[y][x+1] += 1 
        if (x >=1 and x <= 9-1) and (y >= 0 and y <= 9-1):
            if campo[y][x-1] != 'X':
                campo[y][x-1] += 1 
        if (x >= 1 and x <= 9-1) and (y >= 1 and y <= 9-1):
            if campo[y-1][x-1] != 'X':
                campo[y-1][x-1] += 1 
 
        if (x >= 0 and x <= 9-2) and (y >= 1 and y <= 9-1):
            if campo[y-1][x+1] != 'X':
                campo[y-1][x+1] += 1 
        if (x >= 0 and x <= 9-1) and (y >= 1 and y <= 9-1):
            if campo[y-1][x] != 'X':
                campo[y-1][x] += 1 
 
        if (x >=0 and x <= 9-2) and (y >= 0 and y <= 9-2):
            if campo[y+1][x+1] != 'X':
                campo[y+1][x+1] += 1 
        if (x >= 1 and x <= 9-1) and (y >= 0 and y <= 9-2):
            if campo[y+1][x-1] != 'X':
                campo[y+1][x-1] += 1 
        if (x >= 0 and x <= 9-1) and (y >= 0 and y <= 9-2):
            if campo[y+1][x] != 'X':
                campo[y+1][x] += 1
    return campo

def gerarMapaDeJogo():
    campo = [['-' for linha in range(9)] for coluna in range(9)]
    return campo


def mapaJogo(mapa):
    for linha in mapa:
        print(" ".join(str(casa) for casa in linha))
        print("")

        
def verificacao(mapa):
    for linha in mapa:
        for casa in linha:
            if casa == '-':
                return False
    return True


def continuar_jogo():
    resposta = int(input('Deseja continuar o jogo? 1 - Sim.   2 - Não.    :'))
    if resposta == 2:
        return False
    elif resposta == 1:
        return True
    else:
        return False


def main():
        mapa = geradorCampo()
        mapa_do_jogador = gerarMapaDeJogo()

        while True:
            if verificacao(mapa_do_jogador) == False:
                print("Qual Casa vc deseja abrir?")
                x = input("Coluna (de 1 até 9) :")
                y = input("Linha (de 1 até 9) :")
                voldo = input('Digite "n" para sair: ')
                if x == '':
                    print('Você não digitou o numero da coluna!')
                    print('=-'*30)
                    continue
                if y == '':
                    print('Você não digitou o numero de linhas!')
                    print('=-'*30)
                    continue
                x = int(x) - 1
                y = int(y) - 1
                if voldo == 'n':
                    break
                if x >= 8:
                    print('O número de colunas é maior que o limite!')
                    print('=-'*30)
                    continue
                if y >= 8:
                    print('O número de linhas é maior que o limite!')
                    print('=-'*30)
                    continue
                if mapa_do_jogador[y][x] != '-':
                    print('=-'*20)
                    print('Você já abriu essa casa antes!')
                    print('=-'*20)
                    continue
               
                if (mapa[y][x] == 'X'):
                    mapaJogo(mapa)
                    print("Você Perdeu o Jogo")
                    if continuar_jogo() == False:
                        break   

                mapa_do_jogador[y][x] = mapa[y][x]
                mapaJogo(mapa_do_jogador)
                    
 
            else:
                mapaJogo(mapa_do_jogador)
                print("Você Ganhou! Parabéns")
                if continuar_jogo() == False:
                    break
# Start of Program
main()