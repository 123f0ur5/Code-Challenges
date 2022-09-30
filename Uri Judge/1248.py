n = int(input())

for _ in range(n):
    c = False
    dietplan = list(input())
    breakfeast = list(input())
    dinner = list(input())
    
    for x in breakfeast:
        if x not in dietplan:
            c = True
            break
        if x in dietplan:
            while dietplan.count(x) != 0:
                dietplan.remove(x)
    
    if not c:
        for x in dinner:
            if x not in dietplan:
                c = True
                break
            if x in dietplan:
                while dietplan.count(x) != 0:
                    dietplan.remove(x)
    
    if c:
        print('CHEATER')
    else:
        print(''.join(sorted(dietplan)))