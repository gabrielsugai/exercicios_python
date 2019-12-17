while True:
  try:
  	x = input().split()
  	x = list(map(int,x))
  	n, amin, amax = x
  	cont=0
  	while n:
  		n-=1
  		y = int(input())
  		if(amin<=y<=amax):
  			cont+=1
  	print(cont)
  except EOFError:
  	break