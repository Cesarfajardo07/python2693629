import random

def llenarListas(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaListas(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def sumaMayor(lista):
    suma1=sumaListas(l1)
    suma2=sumaListas(l2)
    if suma1 > suma2:
        print(f'La suma de la primera lista {suma1} es mayor que la suma de la segunda lista {suma2}')
    else:
        print(f'La suma de la segunda lista {suma2} es mayor que la suma de primera lista {suma1}')











l1=llenarListas(4,10)
l2=llenarListas(4,10)
print(l1)
print(l2)
print(f'La suma de la primer lista es {sumaListas(l1)}')
print(f'La suma de la segunda lista es {sumaListas(l2)}')
print(sumaMayor(l1))











