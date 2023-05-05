import random
suma=0
mayor=1000000
menor=0
promedio=0
lista=[]
tam=int(random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    suma+=num
    promedio=suma/tam

print(lista)
print(f'la suma es {suma}')
print(f'El promedio es {promedio}')



