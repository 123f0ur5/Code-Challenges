#didn't understand the problem

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        x = int(input())
        if x%2!= 0:
            print(2*(x-1))
        else:
            print(2*(x+1))