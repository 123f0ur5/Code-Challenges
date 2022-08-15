c = True

while c:
    sum = 0
    two = 0
    while two != 2:
        a = float(input())

        if a < 0 or a > 10:
            print('nota invalida')
        else:
            sum += a
            two += 1
    
    print('media = {:.2f}'.format(sum/two))

    while True:
        b = float(input('novo calculo (1-sim 2-nao)\n'))
        if b == 1:
            break
        elif b == 2:
            c = False
            break