import operator
ans = []
num = []

while True:
    n = int(input())
    if n == 0:
        break
    lst = [[] for _ in range(n)]
    for i in range(n):
        name = input()
        color, lenght = input().split()
        lst[i].append(color)
        lst[i].append(lenght)
        lst[i].append(name)

    lst = sorted(lst, key = operator.itemgetter(2))
    lst = sorted(lst, key = operator.itemgetter(1), reverse=True)
    lst = sorted(lst, key = operator.itemgetter(0))

    ans.append(lst)
    num.append(n)

for i in range(len(num)):
    for j in range(len(ans[i])):
        print(' '.join(ans[i][j]))
    if i < len(num)-1:
        print()