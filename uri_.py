while True:
	try:
		data = ''
		achei = False
		linha = input()
		N,D = linha.split()
		N = int(N)
		D = int(D)
		for i in range(D):
			linha = input().split()
			if linha[1:].count('1') == N and not achei:
				data = linha[0]
				achei = True
		if data != "":
			print(data)
		else:
			print("Pizza antes de FdI")
	except:
		break