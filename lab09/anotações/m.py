def meM():
    m = [[0,0],[1,1]]

    M = len(m[0]) * [len(m)*[0]]

    print(len(M))
    print(len(m))
    return None

def g(x,y):
    acumula = 0
    for i in range(x):
        for j in range(i, y):
            acumula = acumula + y
    return acumula,j

print(g(3,5))


