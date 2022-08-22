mat_values = []

while True:
    m = int(input())
    if m != 0:
        mat_values.append(m)
    else:
        for x in range(len(mat_values)):
            mat = [[1 for _ in range(mat_values[x])] for _ in range(mat_values[x])]
            cont = str(pow(pow(2,mat_values[x]-1),2))
            for i in range(mat_values[x]):
                for j in range(mat_values[x]):
                    if i == 0 and j == 0:
                        mat[i][j] = 1
                    elif i < j:
                        mat[i][j] = mat[i][j-1] * 2
                    else:
                        mat[i][j] = mat[i-1][j] * 2
                    if j == 0:
                        print(str(mat[i][j]).rjust(len(cont)), end='')
                    else:
                        print(str(mat[i][j]).rjust(len(cont)+1), end='')
                print()
            print()
        break