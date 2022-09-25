while True:
    n = int(input())

    if n == 0:
        break

    d1, d2 = map(int, input().split())

    for i in range(n):
        x, y = map(int, input().split())
        if x > d1 and y > d2:
            print('NE')
        elif x < d1 and y < d2:
            print('SO')
        elif x > d1 and y < d2:
            print('SE')
        elif x < d1 and y > d2:
            print('NO')
        elif(x == d1 or y == d2):
            print('divisa')