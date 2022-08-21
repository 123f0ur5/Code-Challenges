sum = 0
med = 0
mat = [[0 for _ in range(12)] for _ in range(12)]
op = input()

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())
        if j > i:
            sum += mat[i][j]
            med += 1

if op == 'M':
    print(f'{sum/med:.1f}')
else:
    print(f'{sum:.1f}')