while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        mat = [['' for _ in range(m)] for _ in range(n)]

        for i in range(n):
            mat[i] = input() 

        a, b = map(int, input().split())
        new_mat = [['' for _ in range(b)] for _ in range(a)]

        for i in range(a):
            for j in range(b):
                new_mat[i][j] = mat[int(i//(a/n))][int(j//(b/m))]
        
        for i in range(a):
            print(''.join(new_mat[i]))
        
        print()