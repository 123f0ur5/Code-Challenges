n = int(input())

for i in range(n):
    a, b = input().split()

    a = a[(len(a)-len(b)):]

    if  b in a:
        print('encaixa')
    else:
        print('nao encaixa')