import math

while True:
    try:
        n, m = map(int, input().split())
        n = math.factorial(n)
        m = math.factorial(m)
        print(n+m)
    except EOFError:
        break