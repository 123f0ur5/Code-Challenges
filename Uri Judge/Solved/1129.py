dct = { 0 : 'A',
        1 : 'B',
        2 : 'C',
        3 : 'D',
        4 : 'E',
}

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n):
        p = b = 0
        q = 0
        question = list(map(int, input().split()))
        for i in range(5):
            if question[i] <= 127:
                q = i
                b += 1
            elif question[i] > 127:
                p += 1
        
        if b != 1:
            print('*')
        elif p != 4:
            print('*')
        else:
            print(dct[q])