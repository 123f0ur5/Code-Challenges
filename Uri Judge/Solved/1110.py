while True:
    n = int(input())
    if n == 0:
        break
    
    lst = [str(x) for x in range(1, n+1)]
    discard = []

    while len(lst) > 1:
        discard.append(lst[0])
        lst.pop(0)
        lst.append(lst[0])
        lst.pop(0)
    
    discard = ', '.join(discard)
    print(f'Discarded cards: {discard}\nRemaining card: {lst[0]}')