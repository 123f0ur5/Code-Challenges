a, b, c, d = map(int, input().split())
minuto = 0
hora = 0
passou = False

if(a == c and b == d):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

while 1:
    if(a == c and b == d):
        break
    passou = True
    minuto += 1
    b += 1
    if(minuto == 60):
        minuto = 0
        hora += 1
    if(b == 60):
        b = 0
        a += 1
    if(a == 24):
        a = 0
if passou:
    print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")