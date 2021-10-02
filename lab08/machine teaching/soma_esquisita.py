import math
def soma():
     '''essa função retorna a soma das fatoriais de um numero n '''
     ''' ->float '''
     n = 10
     lista_resultados = list()
     numerador = 10
     for i in range(1,n+1):
         fatorial = math.factorial(i)
         if numerador%2 == 0:
           lista_resultados.append(numerador/fatorial)
         else:
              lista_resultados.append((numerador/fatorial)*-1)
         numerador -= 1
     return round(sum(lista_resultados),2)
         
print(soma())
