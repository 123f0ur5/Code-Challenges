par = 0
impar = 0
pos = 0
neg = 0

for i in range(0,5):
    a = int(input())
    if(a%2==0):
        par += 1
    else:
        impar += 1
    if(a > 0):
        pos += 1
    elif(a < 0):
        neg += 1

print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)")