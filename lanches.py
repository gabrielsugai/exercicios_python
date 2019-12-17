lanches = [4, 4.50, 5, 2, 1.50]
total = 0
lanche, qtde = input().split(" ")
lanche = int(lanche)
qtde = int(qtde)
total = lanches[lanche-1] * qtde
print("Total: R$ %.2f" %total)