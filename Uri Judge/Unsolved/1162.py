#TLE, same problem as 1088

n = int(input())

for i in range(n):
    cont = 0
    l = int(input())

    lst = list(map(int, input().split()))

    for x in range(l):
        for y in range(l):
            if y < l-1:
                if lst[y] > lst[y+1]:
                    aux = lst[y]
                    lst[y] = lst[y+1]
                    lst[y+1] = aux
                    cont += 1

    print(f'Optimal train swapping takes {cont} swaps.')