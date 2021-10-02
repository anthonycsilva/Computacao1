def altera_frase(frase,palavra,posicao):
#essa função recebe uma frase, uma palavra e uma posição da lista. e retorna, caso já exista a palavra na frase, a mesma palavra só que em maiusculo.
#caso não tenha a palavra, ele retorna a nova palavra dentro da frase na posição escolhida
#string,string,int -> string
    frase = frase.split()
    if(palavra in frase != False):
        posicao_palavra = frase.index(palavra)  
        frase[posicao_palavra] = str.upper(frase[posicao_palavra]) 
        return ' '.join(frase)
    else:
        frase.insert(posicao, palavra)
        return ' '.join(frase)


print(altera_frase('que fazia tudo', 'abacate',0))
