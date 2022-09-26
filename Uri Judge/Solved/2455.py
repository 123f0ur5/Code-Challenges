p1, c1, p2, c2 = map(int, input().split())

p1 *= c1
p2 *= c2
if p1 == p2:
    print('0')
elif p2 > p1:
    print('1')
else:
    print('-1')