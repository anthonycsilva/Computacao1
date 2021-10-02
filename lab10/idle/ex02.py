def mostraEntrada(a,b,c):
    '''Essa função mostra os numeros digitados na tela '''
    ''' int, int, int -> int, int, int'''
    print(f'Primeiro Valor: {a}')
    print(f'Segundo Valor: {b}')
    print(f'Terceiro Valor: {c}')
    return a,b,c
def calcularTrapezio(a,b,c):
    '''Essa função calcula a area do um trapézio '''
    '''int, int,int -> float '''
    mostraEntrada(a,b,c)
    area = ((a+b)*c)/2
    return area
def mult(a,b,c):
    '''essa função multiplica o numeros numeros de entrada por eles próprios'''
    '''int, int, int -> int, int, int'''
    mostraEntrada(a,b,c)
    return a*a,b*b,c*c
def media(a,b,c):
    '''essa função retorna a média de 3 numeros'''
    '''int,int,int -> float'''
    mostraEntrada(a,b,c)
    return (a+b+c)/3
def calculaIntervalo(a,b,c):
    '''essa função calcula a soma entre os invervalos de c até um numero b'''
    '''int, int, int -> int'''
    soma = a
    resultados = list()
    resultados.append(a)
    while soma < b:
        soma = soma + c
        if soma<b:
            resultados.append(soma)
    return sum(resultados)
def main():
    '''função principal, usada para execução de funções secundárias'''
    '''-> boolean'''
    print('1 - Calculando a Area do Trapézio')
    print('2 - Calculando os Multiplos!')
    print('3 - Calculando a Média')
    print('4 - Calculando Soma de Intervalo!')
    print('=-'*20)


    opc = int(input('Digite a Opção Desejada: ')) 
    a = int(input('Digite o Primeiro Numero:'))
    b = int(input('Digite o Segundo Numero:'))
    c = int(input('Digite o Terceiro Numero:'))
    print('=-'*20)

    if(a>b):
        print('Erro, A é maior que B')
        return False
    if( a<0 or b<0 or c<0):
        print('Erro, Não é permitido Números Negativos')
        return False
    if(opc > 4):
        print('Erro, o programa ainda não tem essa opção')
        return False
    else:
        if opc == 1:
                print(f'Calculando a Area do Trapézio!')
                print('Resultado:',calcularTrapezio(a,b,c))
        elif opc == 2:
            print(f'Calculando os Multiplos!')
            print('Resultado:',mult(a,b,c))
        elif opc == 3:
            print(f'Calculando a Média')
            print('Resultado:',media(a,b,c))
        elif opc == 4:
            print('Calculando Soma de Intervalo!')
            print('Resultado:', calculaIntervalo(a,b,c))

    
    return True


main()