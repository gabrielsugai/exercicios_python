s = input()
par = True if(len(s) % 2 == 0) else False
deuruim = False
if par:
    cont = 1
else:
    cont = 0
for i in range(65, 91):
    if s.count(chr(i)) % 2 != 0:
        cont+=1
    if cont == 2:
        deuruim = not deuruim
        break
if cont == 1:
    print("VERDADEIRO")
else:
    print("FALSO")