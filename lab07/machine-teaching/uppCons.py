def uppCons(frase):
    '''essa função recebe uma frase e retorna somente as consoantes em maiusculas'''
    '''string -> string'''
    frase = list(frase)
    i = int()
    while(i<len(frase)):
        if(frase[i] in 'BCDFGJKLMNPQRSTVWXZbchdfgjklçmnpqrstzxZX'):
            if frase[i] == ' ':
                i +=1
            frase[i] = frase[i].upper()
        i += 1
    return ''.join(frase)

print(uppCons('São jóias viúvas, como eu, Capitu'))