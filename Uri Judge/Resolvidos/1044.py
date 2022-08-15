a, b = map(int, input().split())

if(a > b):
    maior = a
    menor = b
else:
    menor = a
    maior = b

if(maior%menor==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")