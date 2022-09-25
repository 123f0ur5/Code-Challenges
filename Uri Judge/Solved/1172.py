vet = []
for i in range(10):
    n = int(input())

    if n <= 0:
        vet.append(1)
    else:
        vet.append(n)

for x, y in enumerate(vet):
    print(f'X[{x}] = {y}')