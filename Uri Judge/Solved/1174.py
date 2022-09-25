dct = {}
for i in range(100):
    n = float(input())

    if n <= 10:
        dct[i] = n

for key, value in dct.items():
    print(f'A[{key}] = {value}')