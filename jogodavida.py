matriz = []
l,c = input().split()
l = int(l)
c = int(c)
for i in range(l):
    matriz.append(input())
t = int(input())
cont = 0
for i in range(len(matriz)):
    for j in range(c):
        if matriz[i][j]=='1':
            print(matriz[i-1][j-1:j+2] + matriz[i][j-1] + matriz[i][j+1] + matriz[i+1][j-1])