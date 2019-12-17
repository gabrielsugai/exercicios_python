x = input().split()
a = int(x[0])
b = int(x[1])

h = 0

if a == b:
	h = 24
elif b < a:
	for i in range(a,24):
		h+=1
	for i in range(0,b):
		h+=1
elif a < b:
	for i in range(a,b):
		h+=1

print("O JOGO DUROU %i HORA(S)" %(h))