while True:
    a, b = map(int, input().split())
    soma = 0
    if a <= 0 or b <= 0:
        break

    if a >= b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    
    for i in range(menor, maior+1):
        print(f'{i}',end=' ')
        soma += i

    print(f'Sum={soma}')