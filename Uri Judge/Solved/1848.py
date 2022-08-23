caw = 0
cont = 0
result = []
while caw != 3:
    s = input()
    if s == 'caw caw':
        caw += 1
        result.append(cont)
        cont = 0
    if s[0] == '*':
        cont += 4
    if s[1] == '*':
        cont += 2
    if s[2] == '*':
        cont += 1
print(f'{result[0]}\n{result[1]}\n{result[2]}')