v = int(input('Digite a velocidade: '))
if v > 110:
    print('voce foi multado')
    m = (v - 110) * 5
    print('sua multa é de %d' %m)
    