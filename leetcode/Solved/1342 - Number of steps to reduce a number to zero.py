num = int(input())

passos = 0

while(num != 0):
    if(num%2==0):
        num /= 2
        passos += 1
    else:
        num -= 1
        passos += 1

print(passos)
