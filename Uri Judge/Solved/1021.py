#a = float(input())
#print("NOTAS:")
#print("{} nota(s) de R$ 100.00".format(int(a/100)))
#print("{} nota(s) de R$ 50.00".format(int(a%100/50)))
#print("{} nota(s) de R$ 20.00".format(int(a%100%50/20)))
#print("{} nota(s) de R$ 10.00".format(int(a%100%50%20/10)))
#print("{} nota(s) de R$ 5.00".format(int(a%100%50%20%10/5)))
#print("{} nota(s) de R$ 2.00".format(int(a%100%50%20%10%5/2)))
#print("MOEDAS:")
#print("{} moeda(s) de R$ 1.00".format(int(a%100%50%20%10%5%2)))
#print("{} moeda(s) de R$ 0.50".format(int(a%100%50%20%10%5%2%1/0.5)))
#print("{} moeda(s) de R$ 0.25".format(int(a%100%50%20%10%5%2%1%0.5/0.25)))
#print("{} moeda(s) de R$ 0.10".format(int(a%100%50%20%10%5%2%1%0.5%0.25/0.1)))
#print("{} moeda(s) de R$ 0.05".format(int(a%100%50%20%10%5%2%1%0.5%0.25%0.1/0.05)))
#print("{} moeda(s) de R$ 0.01".format(int(a%100%50%20%10%5%2%1%0.5%0.25%0.1%0.05/0.01)))


a = float(input())
valores = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
notas = True
moedas = True

i = int(0)
while i < len(valores):
    if(i < 6):
        if(notas):
            print("NOTAS:")
            notas = False
        print(f"{int(a/valores[i])} nota(s) de R$ {valores[i]}.00")
        a -= a - a%valores[i]
        i += 1
    else:
        if(moedas):
            print("MOEDAS:")
            moedas = False
            a += 0.001
        print("{} moeda(s) de R$ {:.2f}".format(int(a/valores[i]),valores[i]))
        a -= a - a%valores[i]
        i+= 1