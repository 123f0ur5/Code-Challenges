from tkinter import Y


x = int(input())
y = int(input())
soma = 0

if(x>y):
    maior = x
    menor = y
else:
    menor = x
    maior = y

for i in range(menor,maior+1):
    if i%13 != 0:
        soma += i

print(soma)