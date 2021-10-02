def ano_chines(ano):
#essa função verifica o ano que foi colocado
#int -> list ( array )
    animal =['macaco','galo','cão','porco','rato','boi','tigre','coelho','dragão','serpente','cavalo','carneiro']
    num = ano%12
    return animal[num]