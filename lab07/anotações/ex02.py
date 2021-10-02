import random
def bagulho_random():
    n = 0
    soma = 0
    c = 0
    while(n != 5):
        c = c + 1
        soma = soma + n
        n = random.randint(1,10)
        print(soma)
    print(f'O código foi executado {c} vezes')
    return print(f'Foi gerado o numero {n}. A Operação foi parada')


bagulho_random()