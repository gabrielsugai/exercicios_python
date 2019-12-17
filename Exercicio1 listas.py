notas = [1,2,3,4,5]
x = 0
soma = 0
while x < 5:
	soma += notas[x]
	x += 1
print('Media das notas: %.2f' %(soma/5))