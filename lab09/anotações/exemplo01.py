def conta_ocorrencias_v2(frase, letra):
    palavras = str.split(frase)
    ocorrencias = []
    for palavra in palavras:
        qtd = str.count(palavra, letra)
        ocorrencias.append(qtd)
    return ocorrencias




print(conta_ocorrencias_v2('eu amo python', 'o'))

# O comando str.count() percorre a string, posição por posição e verifica os carecteres, ou seja, é um laço aninhado!

def conta_ocorrencias_v3(frase, letra):
    palavras = str.split(frase)
    ocorrencias = list()
    for palavra in palavras:
        qtd = 0
        for c in palavra:
            if c == letra:
                qtd += 1
        list.append(ocorrencias, qtd)

    return ocorrencias

print('=-'*20)
print(conta_ocorrencias_v3('eu amo python', 'o'))

#essa função foi feita usando um laço aninhado explicito !

