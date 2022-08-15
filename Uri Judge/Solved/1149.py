a = input().split()
x = int(a[0])
soma = 0
a.pop(0)

for i in a:
    if int(i) > 0:
        y = int(i)

for i in range(0, y):
    soma += x + i

print(soma)