def mat_sort(m, mat):
    for i in range(m):
        for j in range(m):
            if j > i:
                mat[i][j] = mat[i][j-1] + 1 
            if j < i:
                mat[i][j] = mat[i-1][j] + 1
    return mat

mat_value = []

while True:
    m = int(input())
    if m != 0:
        mat_value.append(m)
    elif m == 0:
        for x in range(len(mat_value)):
            mat = [[1 for _ in range(mat_value[x])] for _ in range(mat_value[x])]
            mat = mat_sort(mat_value[x], mat)
            for i in range(mat_value[x]):
                for j in range(mat_value[x]):
                    if j != 0:
                        print(str(mat[i][j]).rjust(4), end='')
                    else:
                        print(str(mat[i][j]).rjust(3), end='')
                print()
            print()
        break