from math import sqrt
call = [0, 2, 4]
x = int(input()) 
    
for i in range(x):
    n = int(input())
    fib = 1/sqrt(5) * (pow(1 + sqrt(5), n) / pow(2,n)) - (pow(1 - sqrt(5), n) / pow(2,n))
    fib += 0.3

    print(len(call))
    while n > len(call):
        pos = len(call)
        ans = call[pos-1] * 2 - call[pos-3]
        call.append(ans)

    print(call)
    print(f'fib({n}) = {call[n-1]} calls = {int(fib)}')