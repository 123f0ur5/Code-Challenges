#review tomorrow

def convert(str):
    list1=[]
    list1[:0]=str
    return list1

n = int(input())
ans = []

for i in range(n):
    p = True
    dietplan = input()
    dietplan = convert(dietplan)
    breakfeast = input()
    if breakfeast != '':
        breakfeast = convert(breakfeast)
        for x in breakfeast:
            if x not in dietplan:
                ans.append('CHEATER')
                p = False
            else:
                while dietplan.count(x) != 0:
                    dietplan.remove(x)

    diner = input()
    if diner != '':
        diner = convert(diner)
        for x in diner:
            if x not in dietplan:
                ans.append('CHEATER')
                p = False
            else:
                while dietplan.count(x) != 0:
                    dietplan.remove(x)
    
    if p:
        ans.append(''.join(sorted(dietplan)))

for x in ans:
    print(x)