en = input().split()

a = int(en[0])

b = int(en[1])



a = int(input('Informe A: '))
b = int(input('Informe B: '))
c = int(input('Informe C: '))

maior = (a+b+(abs(a-b)))/2

if c > maior:
    maior = c

print("%i eh o maior" %maior)