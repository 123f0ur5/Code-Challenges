x, y = map(int, (input().split()))
i = 1

while True:
    if i == y+1:
        break
    
    for j in range(0,x):
        if i == y+1:
            break
        elif j != x-1:
            print(i,end=' ')
            i += 1
        else:
            print(i,end='')
            i += 1
    
    print()