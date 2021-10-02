def lingua_p(palavra):
    '''essa função recebe uma palavra e retorna ela na lingua p'''
    '''string -> string'''
    stringFinal = ''
    for i in palavra:
        if i in 'aeiouAEIOUáéíóú':
            stringFinal += i + 'p' + i
        else:
            stringFinal += i
    return stringFinal


print(lingua_p('exemplo'))