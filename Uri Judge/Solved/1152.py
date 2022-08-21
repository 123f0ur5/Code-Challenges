s = 1
x = 2
y = 3

for i in range(1, 20):
    s += y/x
    y += 2
    x *= 2
    
print(f'{s:.2f}')