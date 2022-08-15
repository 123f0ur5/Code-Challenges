from re import X


a = int(input())

for i in range(0,a):
    soma = 0

    x,y = map(int, input().split())

    if x >= y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    
    for z in range(menor, maior):
        if(z%2!=0 and z != maior and z != menor):
            soma += z
    print(soma)