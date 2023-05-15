import random
#camell case se usa para darle nombre a variables funciones etc
#una variable se puede usar en cualquier parte siemprey cuando este afuera de las funciones
#return se usa para  indicar el final de la funcion y para hacer la llamada de la funcion cuando se requiera
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista) #Se usa return para llamar la suma realizada anteriormente y no tener que volver a hacerla, ahi mismo se realiza la division

l1=llenarLista(3,10) #print(llenarLista(l1,5,100)  otra opcion para hacerlo
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1), 2)) #se usa para decidir cuantos numeros del decimal quiere que imprima   #print(promedioLista(l1)) tambien se puede imprimir asi




def numeroMayor(lista):
    mayor=0
    for a in lista:
        if a > mayor:
            mayor=a
    for b in lista:
        if b > mayor:
            print
    return mayor

print(f'El numero mayor de las dos listas es {numeroMayor()}')
