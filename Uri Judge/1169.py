n = int(input())

for i in range(n):
    total = 0
    g = 1
    x = int(input())

    for i in range(x):
        total += g
        g *= 2
    
    total = int(total/12/1000)
    print(f"{total} kg")