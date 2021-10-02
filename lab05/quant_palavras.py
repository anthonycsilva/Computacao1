def quant_palavras(frase):
    frase_sem_espaco = frase.strip()
    frase_separada = frase_sem_espaco.split()
    return len(frase_separada)



print(quant_palavras('  HunterXhunter não é tão bom assim'))
