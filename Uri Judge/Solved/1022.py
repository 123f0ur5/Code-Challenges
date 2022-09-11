from math import gcd
allans = []
fun = {
    '+' : lambda _ : f'{n1 * d2 + n2*d1}/{d1*d2}',
    '-' : lambda _ : f'{n1 * d2 - n2*d1}/{d1*d2}',
    '*' : lambda _ : f'{(n1*n2)}/{(d1*d2)}',
    '/' : lambda _ : f'{(n1*d2)}/{(n2*d1)}',
}
n = int(input())

for i in range(n):
    ans = []
    s = input().split()
    n1, d1 = int(s[0]), int(s[2])
    n2, d2 = int(s[4]), int(s[6])
    op = s[3]

    res = fun[op](op)
    ans.append(res)
    x, y = map(int, res.split('/'))
    mdc = gcd(x,y)
    x = x / mdc; y = y / mdc
    ans.append(int(x)); ans.append(int(y))
    allans.append(ans)

for i in allans:
    print("{} = {}/{}".format(*i))