nv = int(input())
soma =0
for i in range(nv):
    venda = input().split()
    a = int(venda[0])
    b=float(venda[1])
    soma+=(a*b)
print("%.2f"%soma)
