salario = float(input())
p = 0
if (0<salario<=400):
	p = 0.15
elif (400<salario<=800):
	p = 0.12
elif (800<salario<=1200):
	p = 0.1
elif (1200<salario<=2000):
	p = 0.07
else:
	p = 0.04
print("Novo salario: %.2f" %((salario+(salario*p))))
print("Reajuste ganho: %.2f" %(((salario+(salario*p)))- salario))
p = int(p*100)
print("Em percentual: "+str(p)+" %")

