n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x%2==0:
        x += 1
    sum = 0
    for i in range(y):
        sum += x
        x += 2
        
    print(sum)