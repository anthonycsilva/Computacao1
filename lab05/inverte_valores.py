def retira_pontuacao(frase):
    if '.' in frase:
        frase = frase.replace('.',' ')
    
    if '!' in frase:
        frase = frase.replace('!',' ')

    if '?' in frase:
        frase = frase.replace('?',' ')

    if '...' in frase:
        frase = frase.replace('...',' ')

    if '-' in frase:
        frase = frase.replace('-',' ')

    if ',' in frase:
        frase = frase.replace(',',' ')

    if ':' in frase:
        frase = frase.replace(':',' ')

    if ';' in frase:
        frase = frase.replace(';',' ')
    
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    return  ' '.join(frase)

print(inverte('Nossa, como eu gosto de chocolate.'))