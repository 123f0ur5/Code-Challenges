valores = []
sum = 0
pos = 0

for i in range(0,6):
    a = float(input())
    valores.append(a)
    if(valores[i] >= 0):
        pos += 1
        sum += valores[i]

print("{} valores positivos\n{:.1f}".format(pos,(sum/pos)))