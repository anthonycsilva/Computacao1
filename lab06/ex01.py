

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

print(cria_contato('Bruno Campos', ['2199112233',], 'brunoc91@emailquente.com.br', '@brunocampos91'))


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

print(atualiza_contato(0,1,'2199112233'))




