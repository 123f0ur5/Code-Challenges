while True:
    try:
        h, m = map(str, input().split(':'))
        tempo = int(h)*60 + int(m)
        tempo = 480 - 60 - tempo
        if tempo > 0 or tempo == 0:
            print('Atraso maximo: 0')
        else:
            print('Atraso maximo: {}'.format(abs(tempo)))
    except EOFError:
        break