def mat_sort(x, m, mat):
    for i in range(x,m-x):
        for j in range(x, m-x):
            mat[i][j] = x+1
    if x == m:
        return mat
    else:
        return mat_sort(x+1, m, mat)

mat_value = []

while True:
    m = int(input())
    if m != 0:
        mat_value.append(m)
    elif m == 0:
        for x in range(len(mat_value)):
            mat = [[0 for _ in range(mat_value[x])] for _ in range(mat_value[x])]
            mat = mat_sort(0, mat_value[x], mat)
            for i in range(mat_value[x]):
                for j in range(mat_value[x]):
                    if j != 0:
                        print(str(mat[i][j]).rjust(4), end='')
                    else:
                        print(str(mat[i][j]).rjust(3), end='')
                print()
            print()
        break