lista_contatos = list()

def cria_contato(nome,telefone='',email = '', instagram=''):
#essa função recebe informações sobre o contato e cadastra elas em uma lista.
    if(nome == ''):
        return 'Erro, um nome é necessário para cadastro'
    else:
        if(len(telefone) > 1):
            return 'Erro, somente um telefone pode ser Cadastrado'
        else:
            info = [nome,telefone,email,instagram]
            lista_contatos.append(info)
            return lista_contatos 

def popula_lista():
    '''Essa função popula a lista_contatos, para a utilização dela em outras funções'''
    k = 0
    while k < 10 :
        cria_contato('Bruno Campos', ['2199112233',], 'brunoc91@emailquente.com.br', '@brunocampos91')
        k = k + 1

    k = 0
    while k < 10 :
        cria_contato('Samara Otaka', ['2199112233',], 'brunoc91@emailquente.com.br', '@brunocampos91')
        k = k + 1

    k = 0
    while k < 10 :
        cria_contato('Clara Legal', ['2199112233',], 'brunoc91@emailquente.com.br', '@brunocampos91')
        k = k + 1

    k = 0
    while k < 10 :
        cria_contato('Diego Lolzeiro', ['2199112233',], 'brunoc91@emailquente.com.br', '@brunocampos91')
        k = k + 1

    k = 0
    while k < 10 :
        cria_contato('Samara Legal', ['2199112233',], 'brunoc91@emailquente.com.br', '@brunocampos91')
        k = k + 1
    return 'Lista Populada'



#b

def atualiza_contato(contato, atributo, info):
#essa função atualiza dados em uma lista já existente, e verifica em especifico numero de telefones, para que as condições sejam satisfeitas 
    if(atributo == 1):
        if(info in lista_contatos[contato][atributo] != False ):
            lista_contatos[contato][atributo].remove(info)  
            return lista_contatos
        else:
            lista_contatos[contato][atributo].append(info)
    else:
        lista_contatos[contato][atributo] = info

    return lista_contatos


def busca_contato(lista, nome):
    '''Essa função recebe uma lista específica e retorna as ocorrencias do nome escrito'''
    contador = int()
    i = int()
    nomes_encontrados = list()
    
    while i<len(lista):        
        #
        if(nome in lista[i][0] != True):
            nomes_encontrados.append(lista[i][0])
            contador = contador+1
        i = i+1
        #
    print('=-'*20)
    return print(nomes_encontrados,contador)
popula_lista()
busca_contato(lista_contatos,'Samara')


