#too complex for me atm

from math import ceil, floor

def encode_rail_fence_cipher(string, n):
    index = 0
    increasing = True
    mat = [[] for _ in range(n)]
    ans = ''
    
    for s in string:
        if index == n-1:
            increasing = False
        if index == 0:
            increasing = True
        if increasing:
            mat[index].append(s)
            index += 1
        if not increasing:
            mat[index].append(s)
            index -= 1
    for i in mat:
        ans += ''.join(i)
    
    return ans
    
def decode_rail_fence_cipher(string, n):
    top = 0
    middle = 0
    bottom = 0
    increasing = True
    index = 0
    ans = ''
    if n > 2:
        for i in range(len(string)):
            if index == 0:
                top += 1
                increasing = True
            elif index == n-1:
                bottom += 1
                increasing = False
            else:
                middle += 1
            if increasing: index += 1
            if not increasing: index -= 1
    else:
        top = ceil(len(string)/2)
        bottom = floor(len(string)/2)
    
    test = middle
    print(middle, 'antes')
    if middle / (n-2) >= 2.5:
        middle = ceil(middle / (n-2))
    else:
        middle = floor(middle / (n-2))
    print(middle, 'depois')
    mat = [[] for _ in range(n)]
    mid = middle * (n-2) + top + bottom
    middie = 0
    midd = 0
    print(mid)
    for i in range(n):
        if i == 0:
            for x in range(top):
                mat[i].append(string[x])
        elif i == n-1:
            for x in range(len(string)-bottom, len(string)):
                mat[i].append(string[x])
        else:
            if test%(n-2) < n/2:
                if middie > midd and mid != len(string):
                    midd += 1 
                if mid != len(string) and i >= n/2:
                    middie += 1
                for x in range((top+(i-1)*middle+midd), top+(i*middle)+middie):
                    mat[i].append(string[x])
            elif mid == len(string):
                for x in range((top+(i-1)*middle), top+(i*middle)):
                    mat[i].append(string[x])
            else:
                if i > 0 and i <= test%(n-2):
                    for x in range((top+(i-1)*middle), top+(i*middle)):
                        mat[i].append(string[x])
                else:
                    for x in range((top+(i-1)*middle), top+(i*middle)-1):
                        mat[i].append(string[x])
                pass
    print(mat)
    index = 0
    increasing = True
    for i in range(len(string)):
        if index == n-1:
            increasing = False
        if index == 0:
            increasing = True
        if increasing:
            ans += mat[index][0]
            mat[index].pop(0)
            index += 1
        if not increasing:
            ans += mat[index][0]
            mat[index].pop(0)
            index -= 1
    
    return ans

ans = encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 8) #WECRLTEERDSOEEFEAOCAIVDEN
print(ans)

ans2 = decode_rail_fence_cipher("WDEEFARLREEEVEEDOACICTNSO", 8) #WEAREDISCOVEREDFLEEATONCE
print(ans2)