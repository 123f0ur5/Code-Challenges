##TLE, don't know why

numtestes = 0

while True:
    n = int(input())
    if n == 0:
        break

    ans = {}
    p = c = 0
    for i in range(n):
        x, y = map(int, input().split())
        p += x; c += y
        z = int(y/x)
        if z in ans:
            ans[z] += x
        else:
            ans.update({z : x})
    c = int((c/p)* 10 ** 2) / 10 ** 2 #idk but it get 2 decimals without rounding

    ans = sorted(ans.items(), key = lambda x : x[0])
    
    if numtestes > 0:
        print()
    numtestes +=1

    print(f'Cidade# {numtestes}:')
    for x in range(len(ans)):
        print(f'{ans[x][1]}-{ans[x][0]}', end=' ')
    print(f'\nConsumo medio: {c} m3.')