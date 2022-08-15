a = []
i = 0
contagem = 0

while i != 6:
    a.insert(i, float(input()))
    if(a[i] >= 0):
        contagem += 1
    i += 1

print(f"{contagem} valores positivos")