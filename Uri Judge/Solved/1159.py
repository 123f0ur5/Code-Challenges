while True:
    n = int(input())

    if n == 0:
        break

    if n%2!=0:
        n += 1
    sum = 0
    for i in range(5):
        sum += n
        n += 2
    
    print(sum)