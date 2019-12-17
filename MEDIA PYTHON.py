x = 1
soma = 0
while x <= 10:
    v = int(input("[%d°]Informe 10 valores: " %x))
    soma += v
    x += 1
media = soma / 10
print('Media = %.2f' %media)
    