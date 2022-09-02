#Error 100%

lst = [[]]
x = 0
while True:
    try:
        n = int(input())
        lst += []
        print(lst)
        for i in range(n):
            value = input()
            lst[x].append(value)

        print(lst)
        lst[x].sort(reverse=True)
        lst[x] = ''.join(lst[x])
        x += 1
    except EOFError:
        for i in range(lst):
            for j in range(lst[i]):
                print(lst[i][j])