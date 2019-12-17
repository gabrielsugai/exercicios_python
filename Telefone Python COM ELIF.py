min = int(input('Minutos: '))
if min < 200:
    preco = 0.20

elif min <= 400:
    preco = 0.18
elif min > 400 and min <= 800:
    preco = 0.15
else:
    preco = 0.8
print('Valor cobrado: %6.2f' %(min * preco))