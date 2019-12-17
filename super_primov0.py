A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
i = 1
contaA = 0
contaB = 0
contaC = 0

contaA1 = 0
contaB1 = 0
contaC1 = 0

contaA2 = 0
contaB2 = 0
contaC2 = 0

while i <= A:
    if A%i == 0:
        contaA+=1
        i+= 1
i = 1

while i <= B:
    if B%i == 0:
        contaB+=1
        i+= 1
i = 1

while i <= C:
    if C%i == 0:
        contaC+=1
        i+= 1
i = 1

superA = A.split()
superB = B.split()
superC = C.split()

if contaA == 2:
    A1 = int(superA[0])
    while i <= A1:
        if A1%i == 0:
            contaA1+=1
            i+= 1
    A2 = int(superA[1])
    i = 1
    while i <= A2:
        if A2%i == 0:
            contaA2+=1
        i+= 1
    if contaA1 == 2 and contaA2 == 2:
        print("Super")
    else:
        print("Primo")
else:
    print("Nada")
    
if contaB == 2:
    B1 = int(superB[0])
    i = 1
    while i <= B1:
        if B1%i == 0:
            contaB1+=1
        i+= 1
    B2 = int(superB[1])
    while i <= B2:
        if B2%i == 0:
            contaB2+=1
        i+= 1
    if contaB1 == 2 and contaB2 == 2:
        print("Super")
    else:
        print("Primo")
else:
    print("Nada")
    
if contaC == 2:
    i = 1
    C1 = int(superC[0])
    while i <= C1:
        if C1%i == 0:
            contaC1+=1
        i+= 1
    C2 = int(superC[1])
    while i <= C2:
        if C2%i == 0:
            contaC2+=1
        i+= 1
    if contaC1 == 2 and contaC2 == 2:
        print("Super")
    else:
        print("Primo")
else:
    print("Nada")
