total = 0
n = int(input())

for n in range(n):
    a, b = input().split()
    if a == '1001':
        total += 1.5 * int(b)
    elif a == '1002':
        total += 2.5 * int(b)
    elif a == '1003':
        total += 3.5 * int(b)
    elif a == '1004':
        total += 4.5 * int(b)
    elif a == '1005':
        total += 5.5 * int(b)

print(f'{total:.2f}')