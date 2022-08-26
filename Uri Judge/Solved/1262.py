while True:
    try:
        x = 0
        cont = 0
        s = input()
        p = int(input())
        while len(s) != 0:
            if s[0] == 'W':
                cont += 1
                s = s[1:]
            elif s[0] == 'R':
                for i in range(len(s)):
                    if x >= p or s[i] == 'W':
                        break
                    if s[i] == 'R':
                        x += 1
                s = s[x:]
                cont += 1
                x = 0
        print(cont)
    except EOFError:
        break