C = int(input())
i = 0
for i in range(C):
	e1, e2 = input().split(" ")
	if e1 == e2:
		print("empate")

	elif e1 == "tesoura" and e2 == "papel":
		print('rajesh')
	elif e1 == "tesoura" and e2 == "lagarto":
		print('rajesh')

	elif e1 == "pedra" and e2 == "tesoura":
		print('rajesh')
	elif e1 == "pedra" and e2 == "lagarto":
		print('rajesh')

	elif e1 == "papel" and e2 == "pedra":
		print('rajesh')
	elif e1 == "papel" and e2 == "spock":
		print('rajesh')

	elif e1 == "lagarto" and e2 == "papel":
		print('rajesh')
	elif e1 == "lagarto" and e2 == "spock":
		print('rajesh')

	elif e1 == "spock" and e2 == "tesoura":
		print('rajesh')
	elif e1 == "spock" and e2 == "pedra":
		print('rajesh')


	elif e2 == "tesoura" and e1 == "papel":
		print('sheldon')
	elif e2 == "tesoura" and e1 == "lagarto":
		print('sheldon')

	elif e2 == "pedra" and e1 == "tesoura":
		print('sheldon')
	elif e2 == "pedra" and e1 == "lagarto":
		print('sheldon')

	elif e2 == "papel" and e1 == "pedra":
		print('sheldon')
	elif e2 == "papel" and e1 == "spock":
		print('sheldon')

	elif e2 == "lagarto" and e1 == "papel":
		print('sheldon')
	elif e2 == "lagarto" and e1 == "spock":
		print('sheldon')

	elif e2 == "spock" and e1 == "tesoura":
		print('sheldon')
	elif e2 == "spock" and e1 == "pedra":
		print('sheldon')
