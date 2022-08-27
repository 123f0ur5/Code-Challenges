while True:
    try:
        a, b = map(int, input().split())
        print(f'{abs(a-b)}')
    except EOFError:
        break