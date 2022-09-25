def print_numbers(lst, even=False):
    if even:
        for x, y in enumerate(lst):
            print(f'par[{x}] = {y}')
    else:
        for x, y in enumerate(lst):
            print(f'impar[{x}] = {y}')

evenlst = []
oddlst = []
for i in range(15):
    n = int(input())

    if n%2==0:
        evenlst.append(n)
    else:
        oddlst.append(n)
    
    if len(evenlst) == 5:
        print_numbers(evenlst, even=True)
        evenlst.clear()
    if len(oddlst) == 5:
        print_numbers(oddlst)
        oddlst.clear()

print_numbers(oddlst)
print_numbers(evenlst, even=True)