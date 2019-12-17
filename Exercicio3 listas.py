x = 1
vetor = []

while x <= 10:
	n = float(input('Digite o valor %i: ' %x))
	vetor.append(n)
	x+=1
x = 9
while x >= 0:
	print(vetor[x])
	x-=1