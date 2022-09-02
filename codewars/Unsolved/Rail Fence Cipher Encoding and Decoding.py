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
    middle = 0
    increasing = True
    index = 0
    ans = ''
    if n > 2:
        top = floor((len(string)/(n))-1)
        middle = floor(len(string)/(n-1))
        bottom = floor((len(string)/(n))-2)
    else:
        top = ceil(len(string)/2)
        bottom = floor(len(string)/2)
    
    mat = [[] for _ in range(n)]
    mid = middle * (n-2) + top + bottom
    middie = 0
    midd = 0
    for i in range(n):
        if i == 0:
            for x in range(top):
                mat[i].append(string[x])
        elif i == n-1:
            for x in range(len(string)-bottom, len(string)):
                mat[i].append(string[x])
        else:
            if middie > midd and mid != len(string):
                midd += 1 
            if mid != len(string) and i >= n/2:
                middie += 1
            for x in range((top+(i-1)*middle+midd), top+(i*middle)+middie):
                mat[i].append(string[x])
    
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

ans = encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 5) #WECRLTEERDSOEEFEAOCAIVDEN
print(ans)

ans2 = decode_rail_fence_cipher("WCLEESOFECAIVDENRDEEAOERT", 5) #WEAREDISCOVEREDFLEEATONCE
print(ans2)