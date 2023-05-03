#Determinar cuales y cuantos numero perfetos hay entre el 1 y 1000

suma_divisores=0
a=2

for i in range (1,1001):
    if a % i==0:
        print(i)

for i in range(1,1001):
    if  a % i==0:
        suma_divisores+=i

if suma_divisores==a:
    print(f'Los numero perfectos entre 1 y 1000 son {a} ')
