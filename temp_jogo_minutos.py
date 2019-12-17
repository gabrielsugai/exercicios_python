valores = input().split()
valores = list(map(int,valores))

a, b, c, d = valores

inicio = (a*60)+b
fim = (c*60)+d

if fim - inicio == 0:
	h = 24
	m = 0
elif fim-inicio < 60 and fim-inicio > 0:
	h = 0
	m = (fim - inicio)
elif fim - inicio > 60:
	temp = fim - inicio
	h = temp//60
	m = temp-(h*60)
print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))