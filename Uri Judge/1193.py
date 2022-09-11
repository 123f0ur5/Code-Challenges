n = int(input())

for i in range(n):
    s = input().split()
    
    print(f'Case {i+1}:')

    if s[1] == 'bin':
        x = int(s[0], 2)
        print(f'{x} dec')
        print(hex(x).replace('0x','') + ' hex')
    elif s[1] == 'dec':
        print(hex(int(s[0])).replace('0x','') + ' hex')
        print(bin(int(s[0])).replace('0b','')+ ' bin')
    elif s[1] == 'hex':
        x = int(s[0], 16)
        print(f'{x} dec')
        print(bin(x).replace('0b', '') + ' bin')
    
    if i < n-1:
        print()