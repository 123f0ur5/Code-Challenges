a = int(input())

res = [a]

for i in range(1,11):
    res.append(res[i-1]*2)
    print('N[{}] = {}'.format(i-1, res[i-1]))