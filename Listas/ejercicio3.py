import random
rango= 100
tam=int(random.randint(15,20))
lista=[]

lista.append(random.randint(1,rango))
for i in range (tam-1):
    sig_decena= ((lista[-1]// 10 )+1)*10
    nuev_numero=random.randint(lista[-1]+1,min(sig_decena,rango))
    lista.append(nuev_numero)
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