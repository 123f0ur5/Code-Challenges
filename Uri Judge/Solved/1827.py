from math import floor

while True:
    try:
        n = int(input())
        mat = [ [0 for _ in range(n)] for _ in range(n)]
        middle = int(n/3)
        center = floor(n/2)
        aux = n-1
        for i in range(n):
            for j in range(n):
                if i == j:
                    mat[i][j] = 2
                if j == aux:
                    mat[i][j] = 3
                if i >= middle and j >= middle and i < n-middle and j < n-middle:
                    mat[i][j] = 1
                if i == center and j == center:
                    mat[i][j] = 4
            aux -= 1
        for row in mat:
            for column in row:
                print(column,end='')
            print()
        print()

    except EOFError:
        break