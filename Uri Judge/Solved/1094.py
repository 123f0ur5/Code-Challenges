a = int(input())
total = 0
ratos = 0
coelhos = 0
sapos = 0

for i in range(0, a):
    b, c = map(str ,input().split())
    if(c == 'R'):
        ratos += int(b)
    elif(c == 'S'):
        sapos += int(b)
    elif(c == 'C'):
        coelhos += int(b)
    total += int(b)

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format(coelhos*100/total))
print("Percentual de ratos: {:.2f} %".format(ratos*100/total))
print("Percentual de sapos: {:.2f} %".format(sapos*100/total))