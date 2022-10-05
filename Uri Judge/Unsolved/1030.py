n = int(input())

for i in range(n):
    
    n, m = map(int, input().split())
    cont = m-1
    ppl = list(range(1, n+1))

    while len(ppl) != 1:
        ppl.pop(cont)
        cont = (cont + (m-1)) % len(ppl)
    print(ppl)