a = int(input())
pessoas = []

for i in range(a):
    q, p = map(int, input().split())
    pessoas.clear()
    contador = 0
    for x in range(q):
        pessoas.append(x+1)
    for y in range(q-1):
        for z in range(p):
            if contador >= len(pessoas):
                contador = 0
            else:
                contador += 1
        print(contador)
        pessoas.pop(contador)
        print(pessoas)
    
    print(f"Case {i+1}: {pessoas[0]}")