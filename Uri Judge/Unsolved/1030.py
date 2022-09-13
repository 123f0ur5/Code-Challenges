a = int(input())


for i in range(a):
    q, p = map(int, input().split())
    pessoas = [x for x in range(1,q+1)]
    contador = 0
    print(pessoas)
    for x in range(q-1):
        contador += p-1
        if contador > len(pessoas)-1:
            contador = contador - contador + p
        print(contador)
        pessoas.pop(contador)
        print(pessoas)
    
    print(f"Case {i+1}: {pessoas[0]}")