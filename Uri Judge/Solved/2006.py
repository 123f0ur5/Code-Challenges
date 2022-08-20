t = input()
a = []
a = input().split()

acertos = 0

for i in a:
    if i == t:
        acertos += 1

print(acertos)