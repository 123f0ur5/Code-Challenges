sum = 0
mat = [[0 for _ in range(12)] for _ in range(12)]
l = int(input())
op = input()

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())
        if j == l:
            sum += mat[i][j]

if op == 'M':
    print(f'{sum/len(mat[l]):.1f}')
else:
    print(f'{sum:.1f}')