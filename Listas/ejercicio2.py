#Buscar un numero ingresado por teclado en la lista
#decir si esta
#decir si esta repetido y cuantas veces
#Posiciones donde lo encontro
#datos dentro de lista de 0 a 9, tamaño lista de 15 a 20
import random
r=0 #Repeticiones
tam=int(random.randint(15,20))
lista= [random.randrange(0,9) for i in range (tam)]
print(lista)

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print(lista)
for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista)

a=int(input( 'Ingrese el numero que desea buscar '))
print(lista)


if a in lista:
    print('El numero que ingreso esta en la lista')
else:
    print('El numero que ingreso no esta en la lista')

for i in range (len(lista)):
    x=lista[i]
    print(lista.index(x))












