import random
def dados():
    '''essa função simula numeros de 2 dados e mostra quantas vezes foram jogados até sair um número repetido'''
    c = int()
    igual = bool()
    while igual == False:
        dado1 = random.randint(1,5000)
        dado2 = random.randint(1,5000)
        c = c + 1
        print(f'Dado1: {dado1}')
        print(f'Dado2: {dado2}')
        print(f'Contador: {c}')
        print('=-'*20)
        if dado1 == dado2 :
            igual = True
            return print(f'Os Dados são iguais! ')
dados()