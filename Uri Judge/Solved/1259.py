from re import X


odd = []
even = []
n = int(input())

for i in range(n):
    x = int(input())
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
    
even.sort()
odd.sort(reverse=True)

for y in even:
    print(y)
for y in odd:
    print(y)