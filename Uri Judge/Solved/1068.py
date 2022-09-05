while True:
    try:
        cont = 0
        s = input()

        for x in s:
            if x == '(':
                cont += 1
            elif x == ')':
                cont -= 1
            if cont < 0:
                break

        if cont == 0:
            print('correct')
        else:
            print('incorrect')
        
    except EOFError:
        break