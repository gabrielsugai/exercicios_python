aux = 0
media = 0.0
for i in range(6):
	x = float(input())
	if x > 0:
		aux+=1
		media+=x
print("%i valores positivos" %(aux))
print("%.1f" %(media/aux))