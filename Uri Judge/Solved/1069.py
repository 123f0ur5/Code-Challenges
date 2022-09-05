n = int(input())

for i in range(n):
    cont = 0
    s = input()
    if '.' in s:
        s = s.replace('.', '')
    while '<>' in s:
        cont += s.count('<>')
        s = s.replace('<>', '')

    print(cont)