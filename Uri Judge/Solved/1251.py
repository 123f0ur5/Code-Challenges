ans = []
while True:
    try:
        dict = {}
        s = input()
        for x in s:
            if ord(x) in dict:
                dict[ord(x)] += 1
            else:
                dict[ord(x)] = 1

        dict = sorted(dict.items(), key = lambda x : x[0], reverse = True)
        dict = sorted(dict, key = lambda x : x[1])
        
        ans.append(dict)
    except EOFError:
        break

for z, x in enumerate(ans):
    for y in x:
        print('{} {}'.format(*y))
    if z < len(ans)-1:
        print()