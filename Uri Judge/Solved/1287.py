while True:
    try:
        s = input()
        s = s.replace('o', '0')
        s = s.replace('O', '0')
        s = s.replace('l', '1')
        s = s.replace(' ', '')
        s = s.replace(',', '')
        try:
            s = int(s)
            if s > 2147483647:
                print('error')
            else:
                print(s)
        except:
            print('error')
    except EOFError:
        break