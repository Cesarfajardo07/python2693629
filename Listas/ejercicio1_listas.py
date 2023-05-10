import random
suma=0
mayor=1000000
menor=-1
promedio=0
lista=[]
tam=int(random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    suma+=num
    promedio=suma/tam
    if  num < mayor:
        mayor=num
    if  num > menor:
        menor=num

print(lista)
print(f'la suma es {suma}')
print(f'El numero mayor es {menor}')
print(f'El numero menor es {mayor}')
print(f'El promedio es {promedio}')



