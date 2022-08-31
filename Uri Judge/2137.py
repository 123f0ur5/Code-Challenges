while True:
    try:
        lst = []
        n = int(input())
        for i in range(n):
            x = input()
            lst.append(x)

        lst.sort(reverse=True)
        lst = '\n'.join(lst)
        print(lst)
    except EOFError:
        break