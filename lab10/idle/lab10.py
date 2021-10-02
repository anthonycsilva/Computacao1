import random

'''Questão 1 '''

def dado():
    '''essa função gera numeros aleatórios de um dado e os coloca em uma lista'''
    '''->list'''
    lista_numeros = list()
    i = 0
    n = int(input('Quantos Numeros deseja?'))
    while i<n:
        numero = random.randint(1,6)
        lista_numeros.append(numero)
        i+= 1
    print(lista_numeros)
    return lista_numeros



def conta_faces(lista):
    '''essa função conta quantas faces do dado apareceram durante a execução da função dado'''
    ''' list -> int '''
    resultado = list()
    for i in range(len(lista)):
        if lista[i-1] == lista[i] and lista[i] != lista[i+1]:
            resultado.append(lista[i])
    print(len(resultado))
    return resultado


'''Questão 2'''

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
def main_02():
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


'''Questão 3 '''

lista_contatos = list()
def criaContato():
    '''Essa função cria um contato em uma lista de contatos já existente'''
    '''-> boolean'''
    nome = str(input('Digite o nome a ser inserido: '))
    codigo = str(input('Digite o codigo da pessoa: '))
    cargo = str(input('Digite o cargo da pessoa: '))
    telefone = str(input('Digite o telefone da pessoa: '))

    if nome == '' or codigo == '' or cargo == '' or telefone == '':
        print('Erro, todas as informções precisam ser preenchidas!')
        return False

    else:
        contato = [nome, codigo, cargo, telefone]
        lista_contatos.append(contato)
        return True


def buscaContato():
    '''Essa função procura um contato que contem a informação sobre o cargo correspondente e retorna ao usuário'''
    '''-> boolean'''
    cargo = str(input('Digite o cargo a ser buscado:'))
    resultado = list()
    for contato in lista_contatos:
        if contato[2] == cargo:
            resultado.append(contato)
    if len(resultado) == 0:
        print('Não foram encontrados resultados com o que foi pesquisado')
        return False
    else:
        print(resultado)
        return True



def main():
    '''Função principal, usada para chamada das funções secundárias'''
    '''-> boolean'''
    print('=-'*20)
    print('1 - Criar um Contato')
    print('2 - Buscar um Contato Pelo Cargo')
    print('0 - Fechar o Programa')
    while True:
        opc = int(input('O que deseja fazer ?: '))
        if opc > 2 or opc < 0:
            print('Erro, essa opção não existe!')
        else:
            if opc == 1:
                criaContato()
            elif opc == 2:
                buscaContato()
            elif opc == 0:
                break