n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    res = 1
    if a < b:
        a, b = b, a
    
    while True:
        res = a%b
        if res == 0:
            break
        a, b = b, res

    print(b)