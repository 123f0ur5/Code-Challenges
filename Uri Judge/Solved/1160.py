n = int(input())

for i in range(n):
    cont = 0
    popA, popB, growA, growB = map(float, input().split())

    while popA <= popB:
        popA += int(popA * (growA/100))
        popB += int(popB * (growB/100))
        cont += 1
        if cont > 100:
            break
    if cont > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{cont} anos.')