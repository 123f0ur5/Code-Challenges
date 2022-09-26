n = int(input())

if n == 1:
    lst = [1]
elif n == 2:
    lst = [1, 1]
else:
    lst = [1, 1]
    for i in range(0, n-2):
        aux = lst[0] + lst[1]
        lst.insert(0,aux)
    
for i in range(len(lst)):
    if i == len(lst)-1:
        print(lst[i])
    else:
        print(lst[i], end=' ')