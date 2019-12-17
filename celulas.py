n = int(input())
pi =3.1415
somaArea = 0
for i in range(n):
    x,y,r = input().split()
    r=int(r)
    somaArea+=((r**2)*pi)
    
print("%i\n"%(int(somaArea)))