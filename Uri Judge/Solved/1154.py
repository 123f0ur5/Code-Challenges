soma = 0
i = 0

while True:
    a = int(input())
    if a < 0:
        break
    soma += a
    i += 1

print('{:.2f}'.format(soma/i))
