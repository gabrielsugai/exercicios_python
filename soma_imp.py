x = input().split()
x = list(map(int,x)
x.sort()

a, b = x
soma = 0
aux = a+1

while aux < b:
	if aux%2 !=0:
		soma += aux
		aux +=1
	else:
		aux+=1
print(soma)