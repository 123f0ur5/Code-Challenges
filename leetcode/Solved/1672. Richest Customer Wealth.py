def maximumWealth(accounts):
    total = 0
    richest = 0

    for i in range(0, len(accounts)):
        for j in range(0,len(accounts[i])):
            total += accounts[i][j]
        
        if(total > richest):
            richest = total
        total = 0
    return richest


acc = [[1, 2, 3], [2, 3, 4]]
x = maximumWealth(acc)
print(x)