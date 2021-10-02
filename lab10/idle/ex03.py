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
    
main()
    

