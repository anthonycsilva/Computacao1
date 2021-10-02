def acima_da_media(notas):
#essa função recebe notas e tira a média e retorna numa nova lista.
#list -> list
    media_lista = list()
    media = sum(notas)/len(notas)
    for n in notas:
        if n>media:
            media_lista.append(n)
    media_lista.sort()
    return media_lista


print(acima_da_media([8,9,7]))