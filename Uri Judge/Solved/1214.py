n = int(input())

for i in range(n):
    count = 0
    s = list(map(int, input().split()))

    x = s[0]
    s.pop(0)
    average = sum(s) / x
    for i in s:
        if i > average:
            count += 1
    
    average = count / x * 100
    print(f'{average:.3f}%')