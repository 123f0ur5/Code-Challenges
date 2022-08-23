while True:
    cont = 0
    a, b = map(str, input().split())
    if a == '0' and b == '0':
        break

    if a in b:
        x = b.replace(a, '')
    else:
        x = b
        
    if x != '':
        if x[0] == '0':
            for i in range(len(x)):
                if x[i] == '0':
                    cont += 1
                else:
                    break
    
    x = x[cont:]
    if x == '':
        x = '0'
    
    print(x)