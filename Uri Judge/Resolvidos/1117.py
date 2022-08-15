from re import A


two = 0
sum = 0

while two != 2:
    a = float(input())
    if a < 0 or a > 10:
        print('nota invalida')
    else:
        sum += a
        two += 1

print('media = {:.2f}'.format(sum/two))