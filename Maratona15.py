variaveis = input().split()

x1 = float(variaveis[0])
y1 = float(variaveis[1])
x2 = float(variaveis[2])
y2 = float(variaveis[3])

distancia = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5

print("%.4f" %distancia)