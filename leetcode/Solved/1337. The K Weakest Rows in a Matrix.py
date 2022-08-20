def kWeakestRows(mat, k):
    power = 0
    check_power = 200
    position = 0
    thisdict = {}
    ans = []
    for i in range(0, len(mat)):
        for j in range(0,len(mat[i])):
            power += mat[i][j]
        thisdict.update({i : power})
        power = 0
    for k in range(0, k):
        for x in range(0, len(thisdict)):
            #Got some errors deleting the index from dictionaries and getting ErrorType, so I decided to check if x is in answer
            if  thisdict.get(x) < check_power and x not in ans:
                check_power = thisdict.get(x)
                position = x
        ans.append(position)
        thisdict = thisdict
        check_power = 200
    
    return ans

mat =  [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]

ans = kWeakestRows(mat, 2)
print(ans)