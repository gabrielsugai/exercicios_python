def fatorial(i):
    fat =1
    for j in range(2,i+1):
        fat *=i
    return fat
pi=3.1415
n=0
x=float(input())
R = x*pi/(180)
somatoriataylor = 0.0
for n in range(5):
    taylor = (-1)**n
    taylor*=(R**(2*n))
    taylor/=fatorial(2*n)
    somatoriataylor+=taylor
print("%.3f\n"%somatoriataylor)