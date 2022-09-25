from math import sqrt

x = int(input())

for i in range(x):
    prime = True
    n = int(input())
    if n == 1:
        prime = False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i == 0:
                prime = False
    

    if prime:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')