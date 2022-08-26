n = int(input())

for i in range(n):
    cont = set()
    s = input()

    for x in s:
        if x >= 'a' and x <= 'z':
            cont.add(x)
    
    if len(cont) == 26:
        print('frase completa')
    elif len(cont) >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')