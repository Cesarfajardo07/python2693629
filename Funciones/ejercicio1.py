import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def numeroMayor(lista):










l1=llenarLista(3,10)
print(l1)
print(f'La suma de los valores es la lista es {sumaLista(l1)}')
print('El promedio de la lista es', round(promedioLista(l1), 2))
print(f'El orden descendente de la lista es {ordenDescendente(l1)}')
