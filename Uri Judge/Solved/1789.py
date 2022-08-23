v = []
while True:
    try:
        l = input()

        v = map(int, input().split())
        v = max(v)

        if v < 10:
            print(1)
        elif v >= 10 and v < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break