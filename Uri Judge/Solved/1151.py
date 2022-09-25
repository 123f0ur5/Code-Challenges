n = int(input())

x = 0
y = 1

for i in range(n):
    if i == n-1:
        print(x, end='\n')
    else:
        print(x, end=' ')
    aux = y
    y = y + x
    x = aux