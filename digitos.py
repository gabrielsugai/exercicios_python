from math import sqrt
lista = [0,0,0,0,0,0,0,0,0,0]
teste = int(input())
inter = input().split()
x = int(inter[0])
y = int(inter[1])
primo = True
for i in range(teste):
    for j in range(x,y):
        z = sqrt(j)
        for a in range(2,z):
            if 2%a == 0:
                primo = False
        if primo:
            b = str(j)
        for c in range(10):
            d = b.count(str(c))
            lista[c]+=d
    print("Intervalo %i"%(i+1))
    for xx in range(10):
        print("%i: %i"%(xx,lista[xx]))