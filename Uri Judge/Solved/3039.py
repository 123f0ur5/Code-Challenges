car = 0
doll = 0

n = int(input())

for i in range(n):
    name, sex = input().split()
    if sex.upper() == 'M':
        car += 1
    elif sex.upper() == 'F':
        doll += 1

print(f'{car} carrinhos\n{doll} bonecas')