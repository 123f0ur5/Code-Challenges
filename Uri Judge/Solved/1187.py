sum = 0
med = 0
control = 11
mat = [[0 for _ in range(12)] for _ in range(12)]
op = input()

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())
        if j > i and j < control:
            sum += mat[i][j]
            med +=1
    control -= 1

if op == 'M':
    print(f'{sum/med:.1f}')
else:
    print(f'{sum:.1f}')