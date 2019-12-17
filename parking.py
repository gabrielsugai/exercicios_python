casos = int(input())
for i in range(casos):
    linha = list(map(int,input().split()))
    if  i == 0:
        tempoinicial =linha[0]*60 + linha[1]
        tempofinal = linha[2]*60 + linha[3]
    else:
        tempoinicial = linha[0]*60 + linha[1]if(linha[0]*60 + linha[1]<tempoinicial) else tempoinicial
        tempofinal = linha[2]*60 + linha[3]if(linha[2]*60 + linha[3]>tempofinal) else tempofinal
print(tempofinal-tempoinicial)