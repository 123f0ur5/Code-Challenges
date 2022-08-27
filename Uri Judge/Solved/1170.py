n = int(input())

for i in range(n):
    cont = 0
    c = float(input())

    while c > 1:
        c /= 2
        cont += 1
    
    print(f'{cont} dias')