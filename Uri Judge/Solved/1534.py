mat_values = []
while True:
    try:
        m = int(input())
        mat_values.append(m)
    except EOFError:
        for x in range(len(mat_values)):
            mat = [[3 for _ in range(mat_values[x])] for _ in range(mat_values[x])]
            cont = mat_values[x]-1
            for i in range(mat_values[x]):
                for j in range(mat_values[x]):
                    if i == j:
                         mat[i][j] = 1
                    if j == cont:
                        mat[i][j] = 2
                    print(mat[i][j], end='')
                cont -= 1
                print()
        break