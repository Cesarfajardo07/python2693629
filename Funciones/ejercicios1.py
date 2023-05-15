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
    mayor=0
    for a in lista:
        if a > mayor:
            mayor=a
    return mayor

def numeroMenor(lista):
    menor=100000
    for b in lista:
        if menor > b:
            menor=b
    return menor

def ordenAscendente(lista):
    f=len(lista)
    for c in range(f-1):
        for d in range(c+1,f):
            if lista[c]>lista[d]:
                lista[c],lista[d]=lista[d],lista[c]
    return lista

def ordenDescendente(lista):
    f=len(lista)
    for c in range(f-1):
        for d in range(c+1,f):
            if lista[c]<lista[d]:
                lista[c],lista[d]=lista[d],lista[c]
    return lista

def numeroEsta(lista):
    j=int(input('Ingrese un numero: '))

    if j in lista:
        print('El numero que ingreso esta en la lista')
    else:
        print('El numero que ingreso no esta en la lista')
    return lista







l1=llenarLista(5,10)
print(l1)
print(f'La suma de los valores es la lista es {sumaLista(l1)}')
print('El promedio de la lista es', round(promedioLista(l1), 2))
print(f'El numero mayor es {numeroMayor(l1)}')
print(f'El numero menor es {numeroMenor(l1)}')
print(f'Orden Ascendente {ordenAscendente(l1)}')
print(f'Orden Descendente {ordenDescendente(l1)}')
print(numeroEsta(l1))
