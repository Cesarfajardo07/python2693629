#Llenar una lista con estaturas de 1.50cm hasta 2.00cm, luego crear una funcion parra hallar los quintiles de esta




import random

def llenarLista(tamaño,rango):
    tama=random.randint(15,tamaño)
    while tama==tama:
        tama=random.randint(15,tamaño)
        if tama%5==0:
            lista=[round(random.uniform(1.50,rango),2) for i in range(tama)]   
            return lista

def ordenAscen(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista
        
def quintiles(lista,valor):
    quintile=valor*len(lista)/5
    mayor=int(quintile)
    menor=int((valor-1)*len(lista)/5)
    if len(lista)>=quintile:
        listaQuin=lista[menor:mayor]
        return listaQuin
    else: 
        return f"No se encuentra el quintil"

lista1=llenarLista(100,1.79)
print(ordenAscen(lista1))
print(len(lista1))
x=1

while x!=0:
    x=abs(int(input("Digite el quintil que desea buscar: ")))
    if x>=1 and x<=5:
        print(quintiles(lista1,x))
    elif x==0:
        print("Haz salido correctamente del programa")
    else:
        print("Este numero no es valido")