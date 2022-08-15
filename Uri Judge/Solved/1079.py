a = int(input())

for i in range(0, a):
    b, c, d = map(float, input().split())

    print("{:.1f}".format((b*2+c*3+d*5)/10))