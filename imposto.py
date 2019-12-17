x = float(input())

if(0<x<=2000):
	print("Isento")

elif(2000<x<=3000):
	x-=2000
	print("R$ %.2f" %(x*0.08))
elif(3000<x<=4500):
	aux = x - 3000
	x-=(2000+aux) 
	cobrado = (0.08*x)+(aux*0.18)
	print("R$ %.2f" %(cobrado))
elif x>4500:
	aux = x-4500
	x-=aux
	aux2 = x - 3000
	x-=aux2
	x-=2000
	cobrado = (x*0.08)+(aux*0.28)+(aux2*0.18)
	print("R$ %.2f" %(cobrado))