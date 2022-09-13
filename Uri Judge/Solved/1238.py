n = int(input())

for i in range(n):
    ans = ''
    a, b = input().split()
    if len(a) > len(b):
        maior = len(a)
    else:
        maior = len(b)

    for i in range(maior):
        if len(a) > i: 
            ans += a[i]
        if len(b) > i:
            ans += b[i]

    print(ans)