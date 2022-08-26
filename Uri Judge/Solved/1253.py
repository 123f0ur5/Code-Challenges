n = int(input())

for i in range(n):
    s = input()
    num = int(input())

    s = list(map(ord, s))
    s = list(map(lambda x : x - num, s))
    s = list(map(lambda x : x-64+90 if x < 65 else x, s))
    s = list(map(chr, s))
    print(''.join(s))