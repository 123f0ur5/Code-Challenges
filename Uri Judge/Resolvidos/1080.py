pos = 0
maior = -1
for i in range(1, 101):
    a = int(input())
    if(a > maior):
        maior = a
        pos = i

print(f"{maior}\n{pos}")
