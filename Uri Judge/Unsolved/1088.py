#Tle, try it with merge sort with a counter

while True:
    cont = 0
    lst = []
    lst = list(map(int, input().split()))
    
    if lst[0] == 0 and len(lst) == 1:
        break

    for i in range(len(lst)):
        for j in range(len(lst)):
            if j+1 < len(lst):
                if lst[j] > lst[j+1]:
                    aux = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = aux
                    cont += 1
    print(lst, cont)
    if cont%2==0:
        print('Carlos')
    else:
        print('Marcelo')