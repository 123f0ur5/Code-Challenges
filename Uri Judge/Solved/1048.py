a = float(input())

if(a <= 400):
    percentual = 15
elif(a > 400 and a <= 800):
    percentual = 12
elif(a > 800 and a <= 1200):
    percentual = 10
elif(a > 1200 and a <= 2000):
    percentual = 7
else:
    percentual = 4

print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %"
.format((a + (a*(percentual/100))),(a*(percentual/100)), percentual))