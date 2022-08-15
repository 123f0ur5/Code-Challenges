a, b, c = map(float, input().split())
lista = [a,b,c]
lista.sort(reverse=True)

continua = True

bc4 = pow(lista[1],2) + pow(lista[2],2)

if(lista[0] >= (lista[1]+lista[2])):
    print("NAO FORMA TRIANGULO")
    continua = False
if(pow(lista[0],2) == bc4 and continua):
    print("TRIANGULO RETANGULO")
if(pow(lista[0],2) > bc4 and continua):
    print("TRIANGULO OBTUSANGULO")
if(pow(lista[0],2) < bc4 and continua):
    print("TRIANGULO ACUTANGULO")
if(a == b and b == c and continua):
    print("TRIANGULO EQUILATERO")
elif(a == b or b == c or a == c ):
    print("TRIANGULO ISOSCELES")