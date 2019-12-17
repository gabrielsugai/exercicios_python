x = 0
while x == 0:
    nota = int(input('Informe uma nota de 0 a 10: '))
    if nota > -1 and nota < 11:
        print('nota: %i' %nota)
        x = 1
    else:
        print('Nota invalida, informe outra')