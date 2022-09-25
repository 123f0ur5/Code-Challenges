x = int(input())

for i in range(x):
    prime = True
    n = int(input())
    for i in range(2, int(n/2)+1):
        print(i)
        if n%i == 0:
            prime = False

    if prime:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')