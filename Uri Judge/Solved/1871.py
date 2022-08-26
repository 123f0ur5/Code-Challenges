while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    res = str(n + m)

    print(res.replace('0', ''))