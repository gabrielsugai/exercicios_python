x = input().split()
x[0] = float(x[0])
x[1] = float(x[1])
x[2] = float(x[2])

x.sort(reverse=True)
A = x[0]
B = x[1]
C = x[2]

if A >= (B+C):
	print("NAO FORMA TRIANGULO")
elif (A**2) == ((B**2) + (C**2)):
	print("TRIANGULO RETANGULO")
elif (A**2) > ((B**2)+(C**2)):
	print("TRIANGULO OBTUSANGULO")
elif (A**2) < ((B**2)+(C**2)):
	print("TRIANGULO ACUTANGULO")

if A == B and A == C:
	print("TRIANGULO EQUILATERO")
elif A==B and A!=C:
	print("TRIANGULO ISOSCELES")
elif A == C and A !=B:
	print("TRIANGULO ISOSCELES")
elif B==C and A!=B:
	print("TRIANGULO ISOSCELES")