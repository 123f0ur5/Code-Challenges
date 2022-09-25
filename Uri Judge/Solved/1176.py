t = int(input())

for i in range(t):
    n = int(input())

    if n == 0:
        fib = [0]
    elif n == 1:
        fib = [0, 1]
    else:
        fib = [0, 1]
        for i in range(2,n+1):
            fib.append((fib[i-1] + fib[i-2]))

    print(f'Fib({n}) = {fib[n]}')