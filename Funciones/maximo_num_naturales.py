def numnat (x):
    suma=1
    n=1
    while suma <= maximo:
        suma=suma+n
        n=n+1
    return n-1

maximo = int(input('Ingrese un numero: '))
lista=numnat(-1)
print('El numero natural mas pequeño necesario para superar el maximo es: ',lista)