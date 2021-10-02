#recolher 3 notas
#tratar e tirar a média
#retornar a media e verificar se foi reprovado


def recolherNota():
    n1 = int(input('Digite a primeira Nota!:'))
    n2 = int(input('Digite a segunda Nota!:'))
    n3 = int(input('Digite a terceira Nota!:'))


    return [n1,n2,n3]

def calculaMedia(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma = soma + numeros[i]
    media = soma/len(numeros)
    return media

def verifica(media):
    media = round(media, 2)
    if media >= 7:
        print(f'Vc foi aprovado. Sua média foi dê: {media}')
    else:
        print(f'Vc foi reprovado, Sua média n foi o suficiente: {media}. Boas Festas :)')
    return None

def main():
    notas = recolherNota()
    media = calculaMedia(notas)
    verifica(media)
    return None

