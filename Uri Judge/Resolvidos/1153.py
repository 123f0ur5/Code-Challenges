t = int(input())
x = 0

for i in range(0,1000):
    print(f'N[{i}] = {x}')
    x += 1
    if x == t:
        x = 0