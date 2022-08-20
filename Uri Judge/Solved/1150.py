x = int(input())
xx = x + 1
add = 1
z = -999999999999999999999

while z <= x:
    z = int(input())

while x < z:
    x += xx
    xx += 1
    add += 1

print(add)