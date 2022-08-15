a = float(input())

if(a <= 2000):
    porcentagem = 0
elif(a > 2000 and a <= 3000):
    porcentagem = 8
elif(a > 3000 and a <= 4500):
    porcentagem = 18
else:
    porcentagem = 28

if(porcentagem == 0):
    print("Isento")
elif(porcentagem == 8):
    quantia = (a - 2000) * 0.08
    print("R$ {:.2f}".format(quantia))
elif(porcentagem == 18):
    quantia = ((a - 3000) * 0.18) + (1000 * 0.08)
    print("R$ {:.2f}".format(quantia))
elif(porcentagem == 28):
    quantia = ((a - 4500) * 0.28) + (1000 * 0.08) + (1500 * 0.18)
    print("R$ {:.2f}".format(quantia))